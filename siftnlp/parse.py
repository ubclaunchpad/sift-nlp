import json

"""
JSON format for output should have the structure:

        {"product_name": "Name string",
         "feedback":
           [{"id"  : 1,
            "body": "Body string"
            },
            ...
           ]
        }

"""
# Converts raw (potentially non-strict) JSON into JSON array
# @param {JSON} raw_json: source data containing feedback
# @param {array} strict_json_list: output array for JSON objects
def convert_json(raw_json, strict_json_list):
    for index,obj in enumerate(raw_json):
        strict_json_list.append(dict(id=index,body=obj))

# Creates a JSON object array with ids and text
# @param {JSON} unstandardized_json: bulky input JSON
# @param {JSON} final_json_output: standardized output JSON
# TODO: prototyped for Amazon reviews, generalization needed
def standardize_input(unstandardized_json, final_json_output):
    for obj in unstandardized_json:
        final_json_output.append(dict(id=obj['id'],\
                                 body=obj['body']['reviewText']))

# Dictionary file parser that assumes correct file path arguments
# @param {string} file_path: relative path to file
# @return {string}: one string per line/JSON object in file
def parse_dict_file(file_path):
    f = open(file_path,'r')
    for line in f:
        yield eval(line)
    f.close()
