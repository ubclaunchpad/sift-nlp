RUN_PATH=./
CELERY_PATH=./.celery
TEST_PATH=./tests

init:
	pip2.7 install -r requirements.txt
	mkdir $(CELERY_PATH)

save-dep:
	pip2.7 freeze > requirements.txt

clean:
	find . -type f -name '*.pyc' -exec rm --force {} +
	find . -type f -name '*.pyo' -exec rm --force {} +
	find . -type f -name '*~' -exec rm --force {} +

test:
	pytest -rxs $(TEST_PATH)

run-celery:
	celery -A sift.jobrunner.main worker -l info

run-rabbitmq:
	rabbitmq-server

run-redis:
	redis-server

# These background/stop methods are kept around as legacy, but aren't
# useful since there isn't a good way to start Redis in the background.
# In any case, soon we will be using Docker anyway...
celery-background:
	celery multi start worker -A sift.jobrunner.main \
		--pidfile="$(CELERY_PATH)/%n.pid" \
		--logfile="$(CELERY_PATH)/%n.log"

celery-stop:
	celery multi stop worker --pidfile="$(CELERY_PATH)/%n.pid"

rabbitmq-background:
	rabbitmq-server -detached

rabbitmq-stop:
	rabbitmqctl stop

.PHONY: init test
