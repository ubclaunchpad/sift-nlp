import os
import json
import pytest
# Test context
from context import nlp

############################ Test search_body() ################################

# Tests whether a single word, case insensitive, will be found
# in text body
def test_search_body_one_word_case_insens():
    word = "body"
    text_body = "This is a text body."
    assert nlp.search_body(text_body, word) == 1

# Tests whether a single word, case sensitive, will be found
# in text body
def test_search_body_one_word_case_sens():
    word = "Body"
    text_body = "This is a text body."
    assert nlp.search_body(text_body, word) == 1

# Tests whether a single word, case sensitive and trucated, will be found
# multiple times in text body
def test_search_body_one_word_multi_match():
    word = "Tens"
    text_body = "This is a tensing text body that could contain multiple word\
                 tenses."
    assert nlp.search_body(text_body, word) == 2

# Tests whether a single word, case sensitive and trucated, will be found
# multiple times in text body but only from the beginning of the word
def test_search_body_one_word_multi_match_begin():
    word = "Tens"
    text_body = "This is a tensing text body that could contain multiple word\
                 tenses or stensils."
    assert nlp.search_body(text_body, word) == 2

# Tests whether multiple words will be found in text body
def test_search_body_multiple_words():
    text_body = "This is a negative text body that could contain multiple badly\
                 words and is not innovative."
    f = open(os.getcwd()+'/data/trunc_keywords.txt','r')
    count = 0
    for word in f:
        count += nlp.search_body(text_body,word)
    assert count == 3
    f.close()


########################## Test rate_text_body() ###############################

# Tests whether a rating and id are placed in a dict correctly
def test_rate_text_body():
    assert nlp.rate_text_body(0,0) == dict(id=0,rating=0)


######################## Test sort_by_match_count() ############################

# Checks order of sorted dicts for descending order by rating
def test_sort_by_match_count():
    test_dicts = [dict(id=2,rating=2),
                  dict(id=4,rating=1),
                  dict(id=5,rating=1),
                  dict(id=3,rating=2),
                  dict(id=1,rating=10)]
    nlp.sort_by_match_count(test_dicts)
    assert test_dicts == [dict(id=1,rating=10),
                          dict(id=2,rating=2),
                          dict(id=3,rating=2),
                          dict(id=4,rating=1),
                          dict(id=5,rating=1)]
