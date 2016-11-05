from textblob import TextBlob
import math

# This job analyzes a piece of text for positive and negative sentiment
# Returns an array where position 1 is positive percentage and
# position 2 is negative percentage
def run(text):
    blob = TextBlob(text)
    return(sentiment_polarity(blob))

def sentiment_polarity(blob):
    polarity_scores= []
    for sentence in blob.sentences:
        polarity_scores.append(sentence.sentiment.polarity)
    return(sentiment_results(polarity_scores))

def sentiment_results(polarity_scores):
    polarityProp = []
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
    polarityProp.append(positive_percentage)
    polarityProp.append(negative_percentage)
    return(polarityProp)


