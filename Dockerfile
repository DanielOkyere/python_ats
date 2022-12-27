# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR .

COPY . /usr/src/app

WORKDIR /usr/src/app


RUN pip3 install -r /usr/src/app/requirements.txt

RUN systemctl start mysql

RUN python3 -m src.ats_flask

CMD [ "python3", "-m", "api.V1.app", "run", "--host=0.0.0.0", "ATS_DB_USER=user", "ATS_DB_PWD=password", "ATS_DB_NAME=db" ]
