FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget curl unzip gnupg \
    && wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_125.0.6422.141-1_amd64.deb \
    && apt install -y ./google-chrome-stable_125.0.6422.141-1_amd64.deb \
    && rm google-chrome-stable_125.0.6422.141-1_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

RUN export CHROME_VERSION=125 && \
    export DRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

RUN pip install selenium

WORKDIR /tests
COPY . /tests

CMD ["python", "test_app.py"]
