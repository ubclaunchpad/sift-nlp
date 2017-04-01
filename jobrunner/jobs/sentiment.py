from textblob import TextBlob
import math

# This job analyzes a piece of text for positive and negative sentiment
# Returns an array where position 1 is positive percentage and
# position 2 is negative percentage
def run(text):
    return sentiment_polarity(TextBlob(text))

def sentiment_polarity(blob):
    return sentiment_results([sentence.sentiment.polarity for sentence in blob.sentences])

def sentiment_results(polarity_scores):
    positive = sum(filter(lambda x: x > 0, polarity_scores))
    negative = abs(sum(filter(lambda x: x < 0, polarity_scores)))
    total_polarity = negative + positive

    return dict(pos_pct=((positive / total_polarity) * 100),
                neg_pct=((negative / total_polarity) * 100))
