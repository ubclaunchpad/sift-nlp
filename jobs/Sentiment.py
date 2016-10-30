from textblob import TextBlob
import math

text = '''
What can I say about this place. The staff of the restaurant
is nice and the eggplant is not bad. Apart from that, very uninspired
food, lack of atmosphere and too expensive. I am a staunch vegetarian
and was sorely dissapointed with the veggie options on the menu. Will
be the last time I visit, I recommend others to avoid.
'''

blob = TextBlob(text)

def main():
    sentiment_polarity()

# gets polarity scores for each sentence and appends to an array
def sentiment_polarity():
    polarity_scores= []
    for sentence in blob.sentences:
        polarity_scores.append(sentence.sentiment.polarity)
    sentiment_results(polarity_scores)
    ##print(polarity_scores)

def sentiment_results(polarity_scores):
    negative = 0
    positive = 0
    for score in polarity_scores:
        if score < 0:
            negative += score
        else:
            positive += score
    total_polarity = abs(negative) + positive
    negative_percentage = abs(negative) / total_polarity * 100
    positive_percentage = positive / total_polarity * 100
    print("The positive polarity is " + str(positive_percentage) + "%")
    print("The negative polarity is " + str(negative_percentage) + "%")

if __name__ == "__main__":
    main()
