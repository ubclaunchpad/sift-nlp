from sift.jobs.sample import run as sample
from sift.jobs.sentiment import main as sentiment

registry = {
    'sample': sample,
    'sentiment': sentiment,
}
