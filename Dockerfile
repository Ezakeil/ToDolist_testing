FROM selenium/standalone-chrome:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip \
    && pip3 install selenium

WORKDIR /tests
COPY . /tests

CMD ["python3", "test_app.py"]
