import os
import sys
# Create context for test modules
sys.path.insert(0, os.path.abspath('.'))

from siftnlp import core, nlp, parse
from jobrunner.jobs import sentiment
