import os
import json
import pytest
# Test context
from context import lda_nlp

############################ Test run() ################################

def test_run():
    with open('data/hk_feedback_processed.json', 'r+') as f:
        d = json.load(f)
    fb = dict(fb_id=[fb['fb_id'] for fb in d],
            fb_body=[fb['fb_body'] for fb in d])
    lda_nlp.run(fb)
