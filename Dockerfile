FROM python:2.7.12-wheezy
MAINTAINER Eric Stroczynski <ericstroczynski@gmail.com>

COPY . /opt
RUN apt-get update \
    && apt-get clean \
    && pip install -r /opt/requirements.txt

CMD cd /opt \
    && make run-celery
