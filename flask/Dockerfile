FROM python:3.7

RUN mkdir /flaskr
ADD requirements.txt /flaskr

WORKDIR /flaskr
RUN pip3 install -r requirements.txt
RUN FLASK_APP=flaskr
RUN FLASK_ENV=development

EXPOSE 3000
