FROM python:3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN pip install Flask gevent doi2bib
COPY . $APP_HOME

CMD ["python", "serve.py"]