"""
Sample of a Python NLP job. All jobs should be formatted like this one.

The required components of a Sift NLP job are:
(1) A function with the same name as the file
(2) An explanatation of the JSON-serializable output format of the function
"""

from sift.jobs.registry import register

# This sample processing job function returns a list of the number of words
# in each individual piece of feedback, of the form: [Number]
def sample_job(product):
    return map(lambda f: len(f['body'].split()), product['feedback'])

register('sample', sample_job);
