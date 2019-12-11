FROM openjdk:13-buster

RUN apt upgrade
RUN apt update -y && apt-get install -y python3


WORKDIR /app

COPY ./src /app
COPY sipl-interpreter.jar /executable/sipl-interpreter.jar


EXPOSE 8080
ENTRYPOINT ["python3", "/app/main.py"]
