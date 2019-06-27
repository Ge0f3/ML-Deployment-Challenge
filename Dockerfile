# Format: FROM    repository[:version]
FROM ubuntu:17.04

MAINTAINER Geoffrey 'geoffrey.geofe@gmail.com'

FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN export DYLD_LIBRARY_PATH=/usr/local/mysql/lib

COPY . /app

ENTRYPOINT ["python3"]

CMD [ "manage.py" ]

EXPOSE 5000
EXPOSE 80