FROM python:3.9-slim

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src
