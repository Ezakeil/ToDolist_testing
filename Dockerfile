FROM seleniarm/standalone-chromium:latest

USER root

RUN pip install selenium

WORKDIR /tests

COPY . /tests

CMD ["python", "test_app.py"]
