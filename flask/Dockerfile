FROM python:3.7

RUN mkdir /flask
ADD requirements.txt /flask

WORKDIR /flask
RUN pip3 install -r requirements.txt

EXPOSE 5000
