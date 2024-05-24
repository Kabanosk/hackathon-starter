FROM python:3.9-slim-buster

LABEL authors="Wojciech Fiolka <fiolkawojciech@gmail.com>"


ARG POETRY_VERSION=1.8.1

ENV VIRTUAL_ENV=/app/.venv \ 
    PATH="/app/.venv/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

RUN pip install poetry==${POETRY_VERSION}

COPY poetry.lock pyproject.toml ./

RUN poetry install

RUN apt update

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]