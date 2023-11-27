FROM python:3.10

RUN mkdir /opt/project
WORKDIR /opt/project

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc python3-dev
RUN pip install jupyter

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
