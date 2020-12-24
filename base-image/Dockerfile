# Base image for flask REST api tutorial

FROM continuumio/miniconda3:4.6.14-alpine

ADD requirements.txt /home/app/

WORKDIR /home/app/

RUN "while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt"
