FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install ansible
ADD . /code/
