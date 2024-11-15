FROM python:3.10.4-buster as base

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.toml poetry.lock* /app/

RUN poetry install

EXPOSE 5000

COPY . /app


FROM base as production

ENV FLASK_ENV=production

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]


FROM base as development

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

VOLUME ["/app"]

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
