FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y wget curl unzip gnupg chromium chromium-driver

# Install Selenium
RUN pip install selenium

WORKDIR /tests
COPY . /tests

CMD ["python", "test_app.py"]
