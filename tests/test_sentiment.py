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
    print(sentimentResults)
    assert sentimentResults[0]== 45.23809523809524
    assert sentimentResults[1] == 54.761904761904766
