FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /vizards_docker_image

WORKDIR /vizards_docker_image

ADD . /vizards_docker_image

RUN pip install -r requirements.txt
