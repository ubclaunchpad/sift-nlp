import nltk
import nltk.classify.util
from   nltk.classify import NaiveBayesClassifier
import pickle
from   classifier import extract_features
from   nltk.corpus   import movie_reviews

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)

print classifier.show_most_informative_features(20)

test = "Shutter Island is one of the most well crafted psychological thrillers to come by since Silence Of The Lambs. And it is no coincidence both were brilliantly written novels. Shutter Island is adapted by a book written by Dennis Lehane (wrote gone baby, gone and mystic river). It is a book filled with twists and turns, that will leave the reader dizzy. And, that is what it's film counterpart does to the fullest. Martin Scorsese helms the director chair, in a movie where he is more free than any before. This is Scorsese at his most unrestrained."
#test = "delightful"

for key, val in extract_features(test.split()).iteritems():
     if val == True:
         print key

print test.split()
#print classifier.classify(extract_features(test.split()))
#print classifier.classify(extract_features(movie_reviews.words('pos/cv834_22195.txt')))

classifier_f.close()





