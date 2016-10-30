# Sift NLP

Natural language processing service of the Sift app.

## Setup

### Install `pip` and `virtualenv`

Ubuntu
`sudo apt-get install virtualenv`

OS X
`brew install virtualenv`

Initiate virtual environment, activate it, and code.
```bash
virtualenv -p python2.7 venv
source ./venv/bin/activate
make init
```

Alternatively all these instructions are automated (for \*nix systems) in `setup.sh`. After installing `virtualenv` as instructed above, run in your root `sift-nlp` directory as such:
```bash
chmod +x setup.sh
./setup.sh
```

### Install RabbitMQ

Ubuntu
```
sudo apt-get update
sudo apt-get install rabbitmq-server
```

OS X
```
brew update
brew install rabbitmq
```

Add `/usr/local/sbin` to the path. That's where the RabbitMQ executables are.
```
export PATH=$PATH:/usr/local/sbin
```

Start a RabbitMQ server.
```
rabbitmq-server
```

Set up a user and vhost.
```
rabbitmqctl add_user sift sift
rabbitmqctl add_vhost sift
sudo rabbitmqctl set_permissions -p sift sift ".*" ".*" ".*"
```

## Testing

For test data, go to the Amazon product review [dataset](http://jmcauley.ucsd.edu/data/amazon/) and download any of the datasets (I recommend only one as these are large files) to test your code against.

We will be using the [pytest](http://doc.pytest.org/en/latest/) testing framework which should be installed when you run `make init`. If this does not work, run `pip install pytest` after activating venv.

All tests must be kept in the `tests/` dir. To run your tests, type `make test` in the `Makefile` dir. See `test_{nlp, parse}.py` for examples of tests.

## Running

Sift NLP requires running Celery and RabbitMQ. The `Makefile` specifies a number of scripts for starting each of these in the foreground or background. Type `make run` to start an instance of Celery and RabbitMQ in the background.

## Jobs

Sift NLP is composed of jobs, which are simply functions registered with Celery so they can be run asynchronously and in parallel. You can find a simple example job in `jobrunner/jobs/sample.py`. Jobs accept 0 or more inputs of any JSON-serializable type, and return a JSON-serializable object.
