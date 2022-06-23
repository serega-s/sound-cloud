FROM python:3.9.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTOHNUNBUFFERED 1

RUN pip install --updrade pip

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app