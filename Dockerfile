FROM python:2.7.12-wheezy
MAINTAINER Jordan Schalm <jordan.schalm@gmail.com>

COPY . /opt
RUN pip install -r /opt/requirements.txt

CMD cd /opt && make run-celery
