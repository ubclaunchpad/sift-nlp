import re
import json
from sift.jobrunner.main import app

# Celery job for re_nlp
@app.task()
def run(payload):
    with open("data/trunc_keywords.txt",'r+') as f:
        keywords = f.readlines()
    # Match and rate feedback
    rated_feedback_list = []
    for obj in payload:
        counter = 0
        # counter = reduce(lambda x,y: search_body(body, x) + search_body(body, y), keywords)
        for word in keywords:
            counter += search_body(obj['fb_body'], word)
        rated_feedback_list.append(rate_text_body(obj['fb_id'], counter))
    sort_by_match_count(rated_feedback_list)
    return dict(job_id="re_nlp", response=rated_feedback_list)


# Search text body for a word beginning using regex
# @param {string} text_body: feedback text to search
# @param {string} word: word to use in regex match
# @return {int}: 0 if no matches, num_matches otherwise
def search_body(text_body, word):
    word = word.strip()
    match = r'\b[{0}{1}]{2}\S*'.format(word[0].upper(), word[0].lower(), word[1:])
    check = re.compile(match)
    num_matches = len(check.findall(text_body))
    return 0 if num_matches is None else num_matches

# Assign a rating to feedback based on number of word matches
# @param {int} feedback_id: id of original feedback
# @param {int} match_count: number of words matched in text_body
# @return {dict}: key is id, value is rating
def rate_text_body(feedback_id, match_count):
    return dict(fb_id=feedback_id,fb_rating=match_count)

# Sorts the list of dicts by feedback rating
# @param {list} fb_dict_list: list of dicts with id and rating keys
def sort_by_match_count(fb_dict_list):
    fb_dict_list.sort(key=lambda fb: fb['fb_rating'],reverse=True)
