FROM python:3.10.0rc1-alpine

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src
