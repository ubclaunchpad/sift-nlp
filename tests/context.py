import os
import sys
# Create context for test modules
sys.path.insert(0, os.path.abspath('.'))

from jobrunner.jobs import sentiment, re_nlp, lda_nlp
