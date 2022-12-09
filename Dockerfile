# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR .

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install -r /usr/src/app/requirements.txt

CMD [ "python3", "-m", "src.ats_flask", "run", "--host=0.0.0.0" ]
