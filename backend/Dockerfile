FROM python:3.10.4-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y gcc libssl-dev libcurl4-openssl-dev python3-dev netcat
    # && apk add postgresql-dev gcc python3-dev musl-dev curl-dev libressl-dev jpeg-dev zlib-dev libxml2-dev libxslt-dev 
RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir


COPY . ./


RUN chmod +x /usr/src/app/entrypoint.sh


#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
