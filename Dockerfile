FROM seleniarm/python:3.11-chromium

RUN pip install selenium

WORKDIR /tests
COPY . /tests

CMD ["python", "test_app.py"]
