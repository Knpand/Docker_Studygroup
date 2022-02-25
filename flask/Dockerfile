FROM python:3.7

RUN mkdir /flask
ADD requirements.txt /flask

WORKDIR /flask
RUN pip3 install -r requirements.txt

EXPOSE 3000

CMD ["flask","run","-p","3000","-h","0.0.0.0"]