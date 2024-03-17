# Menggunakan Ubuntu 20.04 sebagai base image
FROM python:3.10-slim

ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8080
ENV TZ="Asia/Jakarta"
RUN ls /usr/share/zoneinfo && \
    cp /usr/share/zoneinfo/Asia/Jakarta /etc/localtime && \
    echo "Asia/Jakarta" >  /etc/timezone
 
EXPOSE 8080

# Update paket dan instal dependensi yang diperlukan
RUN apt-get update && \
    apt-get install -y build-essential

# Upgrade PIP
RUN pip3 install pip --upgrade

# Salin seluruh konten proyek ke dalam container
COPY . /app

# Set working directory ke direktori /app
WORKDIR /app

# Install dependensi dari requirement.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apt autoremove -y

# Eksekusi perintah ketika container berjalan
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]