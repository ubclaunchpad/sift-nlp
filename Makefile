RUN_PATH=./siftnlp
TEST_PATH=./tests

init:
	pip2.7 install -r requirements.txt

save-dep:
	pip2.7 freeze > requirements.txt

clean:
	find . -type f -name '*.pyc' -exec rm --force {} +
	find . -type f -name '*.pyo' -exec rm --force {} +
	find . -type f -name '*~' -exec rm --force {} +

test:
	py.test $(TEST_PATH)

run:
	python $(RUN_PATH)/core.py

.PHONY: init test
