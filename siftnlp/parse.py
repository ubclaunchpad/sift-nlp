import json

"""
JSON format for output should have the structure:

        {"product_name": "Name string",
          "feedback":
          [
            {
              "id"  : 0,
              "body": "Body string"
            },
            {
              "id"  : 1,
              "body": "Another body string"
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
# @param {JSON} json_output: standardized output JSON
# TODO: prototyped for Amazon reviews, generalization needed
def standardize_input(unstandardized_json, json_output):
    for obj in unstandardized_json:
        json_output.append(dict(id=obj['id'],\
                                body=obj['body']['reviewText']))

# Dictionary file parser that assumes correct file path arguments
# @param {string} file_path: relative path to file
# @return {string}: one string per line/JSON object in file
def parse_nonstrict_dict_file(file_path):
    f = open(file_path,'r')
    clean_file = f.read().replace('\n','')\
                         .replace('\r','')\
                         .replace('}{','}\n{')
    for obj in clean_file.split('\n'):
        yield eval(obj)
    f.close()

# Logic splitting parse method, important for unkown validity of input JSON data
# @param {string} file_path: path of file to read and standardize
# @return {JSON} standardized_output: a JSON file with predefined structure
def parse(file_path):
    try:
        f = open(file_path)
        strict_json = json.load(f)
    except ValueError:
        print "Not strict enough. Standardizing..."
        dict_list = parse_nonstrict_dict_file(file_path)
        unstandardized_input = []
        convert_json(dict_list, unstandardized_input)
        standardized_output = []
        standardize_input(unstandardized_input, standardized_output)
    else:
        print "Strict already. Standardizing..."
        def replace_key(json_obj, key_to_replace):
            for key in json_obj.keys():
                if key == key_to_replace:
                    json_obj['body'] = json_obj[key]
                    del json_obj[key]
            return obj
        for obj in strict_json:
            replace_key(obj, 'reviewText')
        standardized_output = strict_json
    finally:
        print "Done!"
        return standardized_output
        if not f.closed():
            f.close()
