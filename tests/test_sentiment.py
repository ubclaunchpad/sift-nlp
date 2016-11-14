import pytest
from context import sentiment

def test_text():
    text = '''
    What can I say about this place. The staff of the restaurant
    is nice and the eggplant is not bad. Apart from that, very uninspired
    food, lack of atmosphere and too expensive. I am a staunch vegetarian
    and was sorely dissapointed with the veggie options on the menu. Will
    be the last time I visit, I recommend others to avoid.
    '''
    sentimentResults = sentiment.run(text)
    assert sentimentResults['pos_pct']== 45.23809523809524
    assert sentimentResults['neg_pct'] == 54.761904761904766
