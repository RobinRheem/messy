FROM python:3.6.6-alpine3.8

# Add GCC Support for alpine releases
RUN apk add build-base

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN ["pip3", "install", "pipenv"]

ENV MESSY_HOME /app/src/messy
WORKDIR $MESSY_HOME

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN ["pipenv", "install", "--deploy", "--system"]

ADD . $MESSY_HOME

EXPOSE 8000

ENTRYPOINT ["gunicorn", "app:app", "-c", "gunicorn.py", "--reload"]

