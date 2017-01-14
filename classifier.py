import nltk
import nltk.classify.util
from   nltk import NaiveBayesClassifier
import random
import pickle
from   nltk.corpus   import movie_reviews


pos = [(movie_reviews.words(fileid), 'positive')
        for fileid in movie_reviews.fileids('pos')]

neg = [(movie_reviews.words(fileid), 'negative')
        for fileid in movie_reviews.fileids('neg')]

# list(tuple(list(keyword), 'positive'|'negative'))
keywords = []

for words, sentiment in pos[:1000] + neg[:1000]:
    filtered_words = []
    for word in words:
        if len(word) >= 4:
            filtered_words.append(word.lower())
    keywords.append((filtered_words, sentiment))

random.shuffle(keywords)

def get_words_in_docs(docs):
    all_words = []
    for words, sentiment in docs:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    #word_features = map(lambda x: x[0], wordlist.most_common(len(wordlist)))
    word_features = list(wordlist.keys())
    return word_features

word_features = get_word_features(get_words_in_docs(keywords))


# tuple(dict('contains(x)': Bool), 'positive'|'negative')
def extract_features(doc):
    doc_words = set(doc)
    features = {}
    for word in word_features:
        features[word] = (word in doc_words)
    return features

def train_classifier():
    training_set = nltk.classify.apply_features(extract_features, keywords[:1000])
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print "Hi"
    # test_set = nltk.classify.apply_features(extract_features, keywords[500:])
    # print nltk.classify.accuracy(classifier, test_set)
    with open("naivebayes.pickle","wb") as f:
        pickle.dump(classifier, f)











