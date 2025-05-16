# Dockerfile
FROM python:3.10-slim

# Cài các gói hệ thống cần thiết cho Chrome + Selenium
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    unzip \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean

# Set biến môi trường cho Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Copy source code vào container
WORKDIR /app
COPY . .

# Cài đặt thư viện Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Port Railway sẽ lắng nghe
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]

