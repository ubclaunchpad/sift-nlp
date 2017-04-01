import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn.feature_extraction import text
# Celery app
from sift.jobrunner.main import app

# Celery job runner
# TODO: validate with a set of curated data for which a set of topics is known
@app.task()
def run(payload):
    fb = dict(fb_id=[fb['fb_id'] for fb in payload],
            fb_body=[fb['fb_body'] for fb in payload])

    df, feat_names  = create_tdm_(fb, columns=fb['fb_id'])
    model           = init_and_fit_lda_(df)
    doc_topics      = model.transform(X=df)

    docs_topics = [dict(doc_id=int(fb['fb_id'][n]),
                        top_topic=doc_topics[n].argmax(),
                        topic_dist=[dict(topic_id=index, freq=round(lh,5))
                                    for index, lh in zip(doc_topics[n].argsort(),
                                                     sorted(doc_topics[n].tolist()))[-3:]])
                   for n in range(len(fb['fb_id']))]

    topics_words = [dict(topic_id=t_id,
                         topic_words=[dict(word=feat_names[word_id], freq=round(dist,5))
                                      for word_id, dist in zip(topic.argsort(),
                                                           sorted(topic.tolist()))[-3:]])
                    for t_id, topic in enumerate(model.components_)]

    payload = dict(doc_topic=docs_topics, topic_word=topics_words)
    return dict(job_id="lda_nlp", payload=payload)



# Create a term document matrix that filters words with > 95% doc freq
# and < 2 occurrences, removes all English 'stop words'
def create_tdm_(feedback, columns=None):
    # NOTE: stop_words are common but unnecessary words removed from a text corpus
    # TODO: use a predetermined vocabulary (manually entered keywords) for topics
    cv = text.CountVectorizer(decode_error='replace',
                              stop_words='english',
                              max_df=0.95,
                              min_df=2)
    tx = cv.fit_transform(feedback['fb_body'])
    feature_names = cv.get_feature_names()
    df = pd.DataFrame(tx.toarray().transpose(),
                      index=feature_names,
                      columns=columns)
    return df, feature_names

# Initialize an LDA model object with 20 topics and 'online' learning method
def init_and_fit_lda_(dataframe, num_topics=20, rand_state=1, learn_method='online'):
    model = decomposition.LatentDirichletAllocation(n_topics=num_topics,
                                                    random_state=rand_state,
                                                    learning_method=learn_method)
    model.fit(X=dataframe)
    return model
