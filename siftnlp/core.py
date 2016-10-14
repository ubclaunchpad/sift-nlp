import os
import sys
import json
# Import utility functions
import nlp
import parse


if __name__ == '__main__':

    cwd = os.getcwd()

    # Set up paths and arguments
    # company_name         = sys.argv[1]
    input_file_path   = sys.argv[len(sys.argv)-1]
    keyword_file_path = cwd+'/data/trunc_keywords.txt'
    # TODO: make output_file_path -> STDOUT
    output_file_path  = cwd+'/data/rated_feedback.json'

    with open(keyword_file_path,'r') as k, open(output_file_path,'w') as o:
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
            rated_feedback_list.append(nlp.rate_text_body(obj['id'], counter))
        nlp.sort_by_match_count(rated_feedback_list)
        # Dump JSON to output file
        json.dump(rated_feedback_list, o)
