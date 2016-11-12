import nltk
import nltk.classify.util
from   nltk.classify import NaiveBayesClassifier
from   nltk.corpus   import movie_reviews


# pos_tweets = [('I love this car', 'positive'),
#               ('This view is amazing', 'positive'),
#               ('I feel great this morning', 'positive'),
#               ('I am so excited about the concert', 'positive'),
#               ('He is my best friend', 'positive')]

# neg_tweets = [('I do not like this car', 'negative'),
#               ('This view is horrible', 'negative'),
#               ('I feel tired this morning', 'negative'),
#               ('I am not looking forward to the concert', 'negative'),
#               ('He is my enemy', 'negative')]

pos = [(movie_reviews.words(fileid), 'positive')
        for fileid in movie_reviews.fileids('pos')]

neg = [(movie_reviews.words(fileid), 'negative')
        for fileid in movie_reviews.fileids('neg')]

#print neg[:3]

# all_words = []
# for cats in movie_reviews.categories():
#     all_words.append(cats)

#all_words = nltk.FreqDist(all_words)
#print documents[0]


keywords = []

for words, sentiment in pos[:100] + neg[:100]:
    filtered_words = []
    for word in words:
        if len(word) >= 4:
            filtered_words.append(word)
    keywords.append((filtered_words, sentiment))

#print keywords[:10]



def get_words_in_tweets(tweets):
    all_words = []
    for words, sentiment in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = map(lambda x: x[0], wordlist.most_common(len(wordlist)))
    #word_features = wordlist.keys()
    #print word_features[-10:]
    return word_features

word_features = get_word_features(get_words_in_tweets(keywords))
#print word_features

def extract_features(doc):
    doc_words = set(doc)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in doc_words)
    return features


training_set = nltk.classify.apply_features(extract_features, keywords)
classifier = nltk.NaiveBayesClassifier.train(training_set)


test = "I loved the movie"
for key, val in extract_features(test.split()).iteritems():
    if val == True:
        print key

print classifier.classify(extract_features(test.split()))












