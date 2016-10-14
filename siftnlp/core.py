import os
import sys
import json
# Import utility functions
import nlp
import parse


if __name__ == '__main__':

    cwd = os.getcwd()

    # Set up paths and arguments
    prod_name         = sys.argv[1]
    input_file_path   = sys.argv[2]
    keyword_file_path = cwd+'/data/trunc_keywords.txt'
    # TODO: make output_file_path -> STDOUT
    output_file_path  = cwd+'/data/feedback_clean.json'

    with open(output_file_path,'w') as o, open(keyword_file_path,'r') as k:
        # Make a list of key words
        keyword_list = []
        for key in k:
            keyword_list.append(key)
        # Convert dictionary list to json file
        standardized_output = parse.parse(input_file_path)
        # Match and rate feedback
        rated_feedback_list = []
        for obj in standardized_output:
            body = obj['body']
            counter = 0
            for word in keyword_list:
                counter += nlp.search_body(body, word)
            rated_feedback_list.append(nlp.rate_text_body(body, counter))
        nlp.sort_by_match_count(rated_feedback_list)
        # Dump JSON to output file
        json.dump(rated_feedback_list, o)
