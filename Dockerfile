FROM python:3.7-stretch

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8"

RUN apt-get update -y && \
     apt-get install -y python-pip \
     python-dev \
     unzip


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN wget -q https://www.vbb.de/media/download/2029/GTFS.zip && \
    unzip GTFS.zip -d /app/transitdata/static/data/ && \
    rm GTFS.zip

ARG DATABASE_URI
ENV DATABASE_URI=$DATABASE_URI

ARG SECRET
ENV SECRET=$SECRET

EXPOSE 5000

ENTRYPOINT [ "python", "run.py" ]
