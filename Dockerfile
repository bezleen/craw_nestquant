FROM python:3.8-slim-bullseye

RUN apt-get update \
    && apt-get install -y gcc vim procps supervisor \
    && apt-get install -y libsm6 libxext6 ffmpeg

COPY requirements.txt /
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r requirements.txt

COPY . /webapps

WORKDIR /webapps

# ENTRYPOINT [ "supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]

