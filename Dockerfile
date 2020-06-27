FROM python:3.6-slim-buster

WORKDIR /app
ADD ./*requirements.txt /app/

COPY requirements.txt /
RUN pip install -r requirements.txt

ADD . /app

CMD PYTHONPATH=src python -m coralclassifier.trainer.training -d /tmp