help:
	@cat Makefile

DOCKER_FILE=Dockerfile

build:
	docker build -t recom-system -f $(DOCKER_FILE) .

bash: build
	docker run --name recom-system-server -it -p 5000:5000 recom-system bash

server: build
	docker run --name recom-system-server -d -p 5000:5000 recom-system
