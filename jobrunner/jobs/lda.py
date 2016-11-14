import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn.feature_extraction import text

# TODO: convert to celery task, define an output format
data_file = "data/hk_feedback_processed.csv"

# Read data in from CSV
# TODO: validate with a set of curated data for which a set of topics is known
feedback = pd.read_csv(data_file, skipinitialspace=True, \
                                  dtype={'fb_id':np.str, 'fb_body':np.str}, \
                                  na_values="NaN", \
                                  keep_default_na=False)

# Random sample of size 1000
rsample = feedback.sample(n=1000)
# Set of ID's from sample
doc_lookup = [fb_id for fb_id in rsample['fb_id']]

# Term document matrix that filters words with > 95% doc freq and < 2 occurrences
# NOTE: stop_words are common but unnecessary words removed from a text corpus
# TODO: use a predetermined vocabulary (manually entered keywords) for topics
cv = text.CountVectorizer(decode_error='replace', \
                          stop_words='english', \
                          max_df=0.95, \
                          min_df=2)
tx = cv.fit_transform(rsample['fb_body'])

feature_names = cv.get_feature_names()
df = pd.DataFrame(tx.toarray().transpose(), index=feature_names, \
                                            columns=doc_lookup)

# Initialize and fit model
num_topics  = 20
rand_state  = 1

model = decomposition.LatentDirichletAllocation(n_topics=num_topics, \
                                                random_state=rand_state, \
                                                learning_method='online')

model.fit(X=df)
doc_topics      = model.transform(X=df)
feedback_docs   = feedback['fb_body'].tolist()

# Top 5 words per topic
for topic_idx, topic in enumerate(model.components_):
    print "Topic {}:".format(topic_idx)
    print "Top 5 words: {}\n".format(", ".join([feature_names[i] for i in topic.argsort()[:-6:-1]]))
# 10 documents with associated topics
for n in range(10):
    topic_most_pr = doc_topics[n].argmax()
    top_n_topics = model.components_[topic_most_pr].argsort()[:-6:-1]
    features = cv.get_feature_names()
    print "Doc: {} (fb_id {}), Topic: {}".format(n, doc_lookup[n], topic_most_pr)
    print "Topic list: {}\n".format(", ".join(features[i] for i in top_n_topics))
