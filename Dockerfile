FROM python:3.7-alpine

WORKDIR /app

COPY ./setup.py .
COPY ./requirements.txt .
COPY ./dev.requirements.txt .
COPY ./snakeskin/__init__.py ./snakeskin/__init__.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r dev.requirements.txt
