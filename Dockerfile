FROM python:3.7-stretch

ENV LANG C.UTF-8

RUN apt-get update -y && \
     apt-get install -y python-pip \
     python-dev \
     curl \
     unzip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ARG FLASK_ENV
ENV FLASK_ENV=${FLASK_ENV}

RUN pip install -r requirements.txt

COPY . /app

RUN curl https://www.vbb.de/media/download/2029/GTFS.zip && \
     unzip GTFS.zip -d app/transitdata/static/data/ && \
     rm GTFS.zip

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]