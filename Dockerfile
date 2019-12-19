FROM python:3.7-stretch

ENV LANG C.UTF-8

WORKDIR /app

RUN apt-get update -y && \
     apt-get -qq -y install python-pip python-dev && \
     curl \
     unzip
     # pipenv install
     # openssh-client \
     # python3-setuptools \
     # python3-wheel \
     # build-essential \

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv venv

RUN python -m venv venv

RUN pip install -r requirements.txt

COPY . /app

RUN curl https://www.vbb.de/media/download/2029/GTFS.zip

RUN unzip GTFS.zip -d app/transitdata/static/data/

RUN rm GTFS.zip

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["run.py"]

# ARG FLASK_ENV
# ENV FLASK_ENV=${FLASK_ENV}