import os
import json
import pytest
# Test context
from context import parse

####### Initialize variables #######
cwd = os.getcwd()


############################ Test convert_json() ###############################

# Test ability of JSON converter to parse loose JSON
# NOTE: also tests parse_nonstrict_dict_file(), which by default must work for
# convert_json() to work
def test_convert_incorrect_json():
    path = cwd+'/tests/test_data/feedback_incorrect_structure.json'
    dict_list = parse.parse_nonstrict_dict_file(path)
    out_list = []
    parse.convert_json(dict_list,out_list)
    assert out_list == [dict(id=0,body=dict(id=0,reviewText="Body string")),
                    dict(id=1,body=dict(id=1,reviewText="Another body string"))]


########################### Test standardize_input() ###########################

# Ensures output format of standardize_input() is actually standardized
def test_standardize_input_correct_input():
    path = cwd+'/tests/test_data/feedback_correct_structure.json'
    standardized_list = parse.parse(path)
    assert standardized_list == [dict(id=0,body="Body string bad"),
                                 dict(id=1,body="Another body string")]


# Ensures output format of standardize_input() is actually standardized
def test_standardize_input_incorrect_input():
    path = cwd+'/tests/test_data/feedback_incorrect_structure.json'
    standardized_list = parse.parse(path)
    assert standardized_list == [dict(id=0,body="Body string"),
                                 dict(id=1,body="Another body string")]
