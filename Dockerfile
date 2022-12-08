# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python_ats

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "src.ats_flask", "run", "--host=0.0.0.0" ]