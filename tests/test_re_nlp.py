import os
import json
import pytest
# Test context
from context import re_nlp

############################ Test search_body() ################################

# Tests whether a single word, case insensitive, will be found
# in text body
def test_search_body_one_word_case_insens():
    word = "body"
    text_body = "This is a text body."
    assert re_nlp.search_body(text_body, word) == 1

# Tests whether a single word, case sensitive, will be found
# in text body
def test_search_body_one_word_case_sens():
    word = "Body"
    text_body = "This is a text body."
    assert re_nlp.search_body(text_body, word) == 1

# Tests whether a single word, case sensitive and trucated, will be found
# multiple times in text body
def test_search_body_one_word_multi_match():
    word = "Tens"
    text_body = "This is a tensing text body that could contain multiple word\
                 tenses."
    assert re_nlp.search_body(text_body, word) == 2

# Tests whether a single word, case sensitive and trucated, will be found
# multiple times in text body but only from the beginning of the word
def test_search_body_one_word_multi_match_begin():
    word = "Tens"
    text_body = "This is a tensing text body that could contain multiple word\
                 tenses or stensils."
    assert re_nlp.search_body(text_body, word) == 2

# Tests whether multiple words will be found in text body
def test_search_body_multiple_words():
    text_body = "This is a negative text body that could contain multiple badly\
                 words and is not innovative."
    with open('data/trunc_keywords.txt','r') as f:
        keywords = f.readlines()
    count = 0
    for word in keywords:
        count += re_nlp.search_body(text_body,word)
    assert count == 3


########################## Test rate_text_body() ###############################

# Tests whether a rating and id are placed in a dict correctly
def test_rate_text_body():
    assert re_nlp.rate_text_body(0,0) == dict(fb_id=0,fb_rating=0)


######################## Test sort_by_match_count() ############################

# Checks order of sorted dicts for descending order by rating
def test_sort_by_match_count():
    test_dicts = [dict(fb_id=2,fb_rating=2),
                  dict(fb_id=4,fb_rating=1),
                  dict(fb_id=5,fb_rating=1),
                  dict(fb_id=3,fb_rating=2),
                  dict(fb_id=1,fb_rating=10)]
    re_nlp.sort_by_match_count(test_dicts)
    assert test_dicts == [dict(fb_id=1,fb_rating=10),
                          dict(fb_id=2,fb_rating=2),
                          dict(fb_id=3,fb_rating=2),
                          dict(fb_id=4,fb_rating=1),
                          dict(fb_id=5,fb_rating=1)]

def test_run():
    with open('data/test_processed.json','r+') as f:
        payload = json.load(f)
    response = [dict(fb_id=1, fb_rating=3),
                dict(fb_id=0, fb_rating=2),
                dict(fb_id=2, fb_rating=0)]
    test_dict = dict(job_id="re_nlp",payload=response)
    assert re_nlp.run(payload) == test_dict
