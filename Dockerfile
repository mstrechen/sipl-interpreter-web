FROM openjdk:11

RUN apt-get upgrade
RUN apt-get update -y && apt-get install -y python3


WORKDIR /app

COPY ./src /app
COPY sipl-interpreter.jar /executable/sipl-interpreter.jar


EXPOSE 8080
ENTRYPOINT ["python3", "/app/main.py"]
