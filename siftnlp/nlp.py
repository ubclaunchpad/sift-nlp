import re

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
    return dict(id=feedback_id,rating=match_count)

# Sorts the list of dicts by feedback rating
# @param {list} fb_dict_list: list of dicts with id and rating keys
def sort_by_match_count(fb_dict_list):
    fb_dict_list.sort(key=lambda fb: fb['rating'],reverse=True)
