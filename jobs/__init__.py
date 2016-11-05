from sift.jobs.sample import run as sample
from sift.jobs.sentiment import run as sentiment

registry = {
    'sample': sample,
    'sentiment': sentiment,
}
