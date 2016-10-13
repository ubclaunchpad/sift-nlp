import json
import sys
# Import utility functions
import nlp
import parse


if __name__ == '__main__':
    # Set up paths and arguments
    prod_name         = sys.argv[1]
    input_file_path   = sys.argv[2]
    keyword_file_path = '../data/keywords.txt'
    output_file_path  = '../data/feedback_clean.json'
    # Get dict objects from file
    feedback_dataset = parse.parse_dict_file(input_file_path)
    keyword_list = []

    with open(output_file_path,'w') as o,\
        open(keyword_file_path,'r') as k:
        # Make a list of key words
        for key in k:
            keyword_list.append(key)
        # Convert dictionary list to json file
        temp = []
        parse.convert_json(feedback_dataset, temp)
        final_output = []
        parse.standardize_input(temp,final_output)
        # Match and rate feedback
        clean_dict_list = []
        for body in final_output:
            counter = 0
            for word in keyword_list:
                counter += nlp.search_body(body,word)
            clean_dict_list.append(nlp.rate_text_body(body,counter))
        nlp.sort_by_match_count(clean_dict_list)
        # Dump JSON to output file
        json.dump(clean_dict_list,o)
