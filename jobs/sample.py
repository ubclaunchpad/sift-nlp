"""
Sample of a Python NLP job. All jobs should be formatted like this one.

The required components of a Sift NLP job are:
(1) A function called `run` that takes one argument
(2) An explanation of what the job does

To make a job available, add it to __init__.py in this directory.
"""

import random

# This sample processing job function returns a random int between 1 and 100
def run(payload):
    random.seed()
    return {'random': random.randint(1, 100)}
