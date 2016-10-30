"""
Sample of a Python NLP job. All jobs should be formatted like this one.

The required components of a Sift NLP job are:
(1) A function called `run` that takes one argument and is annotated by the
    `app.task` decorator.
(2) An explanation of what the job does.

To make a job available, add it to __init__.py in this directory.
"""

import random
from sift.jobrunner.main import app

# This sample processing job function returns a random int between 1 and 100
# and the payload that was sent to it.
@app.task()
def run(payload):
    random.seed()
    return {'random': random.randint(1, 100), 'payload': payload}
