# Sift NLP
[![Build Status](https://api.travis-ci.org/ubclaunchpad/sift-nlp.svg?branch=master)](https://travis-ci.org/ubclaunchpad/sift-nlp)
[![ZenHub](https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png)](https://zenhub.com)

Natural language processing service of the Sift app.

The other components to the Sift app are in these repositories:
The following repositories contain Sift services:
* [sift-base](https://github.com/ubclaunchpad/sift-base)
* [sift-api](https://github.com/ubclaunchpad/sift-api)
* [sift-web](https://github.com/ubclaunchpad/sift-web)


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

### Set up Docker environment

See instructions in [Sift Base](https://github.com/ubclaunchpad/sift-base) for setting up a Docker environment to run Sift. If you can't use Docker for some reason, follow the instructions below for installing and running RabbitMQ and Redis manually.

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

### Install Redis

Ubuntu
```
sudo apt-get update
sudo apt-get install redis
```

OS X
```
brew update
brew install redis
```

Start a Redis server.
```
redis-server
```

## Testing

For test data, go to the Amazon product review [dataset](http://jmcauley.ucsd.edu/data/amazon/) and download any of the datasets (I recommend only one as these are large files) to test your code against.

We will be using the [pytest](http://doc.pytest.org/en/latest/) testing framework which should be installed when you run `make init`. If this does not work, run `pip install pytest` after activating venv.

All tests must be kept in the `tests/` dir. To run your tests, type `make test` in the `Makefile` dir. See `test_{nlp, parse}.py` for examples of tests.

## Running Without Docker

If you can't use Docker for some reason, you can manually run Sift services.

Sift NLP requires running Celery, Redis, and RabbitMQ. You can run each of these by running `make run-celery`, `make run-rabbitmq`, and `make run-redis`,

## Jobs

Sift NLP is composed of jobs, which are simply functions registered with Celery so they can be run asynchronously and in parallel. You can find a simple example job in `jobrunner/jobs/sample.py`. Jobs accept 0 or more inputs of any JSON-serializable type, and return a JSON-serializable object.
