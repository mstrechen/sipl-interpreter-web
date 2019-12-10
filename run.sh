#!/bin/zsh

docker stop  sipl
docker run --rm -p 80:8080 -v ${PWD}/src:/app -it --name sipl sipl-web
