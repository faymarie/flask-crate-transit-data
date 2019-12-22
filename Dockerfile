FROM python:3.7-stretch

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8"

RUN apt-get update -y && \
     apt-get install -y python-pip \
     python-dev \
     curl \
     unzip


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN wget -q https://www.vbb.de/media/download/2029/GTFS.zip && \
    unzip GTFS.zip -d /app/transitdata/static/data/ && \
    rm GTFS.zip

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]
