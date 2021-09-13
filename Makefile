.ONESHELL:

export COMPOSE_FILE ?= docker/docker-compose.yml

build:
	py -m venv .venv
	.venv\Scripts\activate
	pip install -r requirements.txt

run:
	py src/run.py

docker.build:
	${docker-compose} build

docker.run:
	${docker-compose} up

docker-compose = docker-compose --file ${COMPOSE_FILE}
