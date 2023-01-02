# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR .

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install -r /usr/src/app/requirements.txt
# RUN pip3 install sqlalchemy
# RUN python3 -m nltk.downloader all
# RUN python3 -m api.V1.app 
CMD [ "python3", "-m", "src.ats_flask", "run", "--host=0.0.0.0" ]
