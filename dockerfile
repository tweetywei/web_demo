# base image
FROM python:3.8

# set work directory
WORKDIR /app/web_demo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app/web_demo

# install psycopg2 dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

expose 8000

# copy project
COPY src .

# CMD ["sleep", "infinity"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
