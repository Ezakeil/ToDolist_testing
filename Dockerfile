FROM python:3.11-slim

# Install Chrome
RUN apt-get update && apt-get install -y wget curl unzip gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install matching ChromeDriver manually
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/124.0.6367.91/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Selenium
RUN pip install selenium

WORKDIR /tests
COPY . /tests

CMD ["python", "test_app.py"]
