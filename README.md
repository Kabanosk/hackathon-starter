# Hackathon Starter

A simple Python project to get you started with web development and testing using Docker and GitHub Actions.

## Prerequisites

- Python 3.8
- Docker
- Docker Compose
- Poetry

## Overview
- [Getting started](#getting-started)
    - [Clone the repository](#clone-the-repository)
    - [Basic env](#ask-for-the-env-file-to-the-project-owner-or-use-postgres-default-values-in-the-env-file)
- [Setup](#setup)
    - [Virtual environment](#create-a-virtual-environment-and-install-the-dependencies)
    - [Docker setup](#build-the-docker-image-and-run-the-containers)
    - [Testing](#testing)
    - [Stopping containers](#stop-the-containers)
- [Database](#database)
    - [Database changes](#creating-or-updating-tables-in-database)
    - [Migrations](#creating-migrations)
- [Linting](#linting)
- [Github actions](#github-actions)
- [License](#license)

## Getting Started
#### Clone the repository

```bash
git clone https://github.com/yourusername/hackathon-starter.git
cd hackathon-starter
```

#### Ask for the `.env` file to the project owner, or use postgres default values in the `.env` file:

```bash
DB_USER=postgres
DB_PASS=postgres
DB_HOST=db
DB_NAME=postgres
DB_PORT=5432
```
### Setup 
#### Create a virtual environment and install the dependencies

```bash
poetry shell 
```

#### Build the Docker image and run the containers

```bash
docker compose up --build
```

#### Testing
```bash
pytest test/test_api.py  # to test the API
docker exec hackathon-starter-web-1 poetry run pytest tests/test_database.py  # to test the database inside the container
```

Or run all tests with `docker exec -it hackathon-starter-web-1 pytest
`

#### Stop the containers

```bash
docker compose down
```
### Database
#### Creating or updating tables in database
To create new table in database just create needed class in `src/model/tables.py` similar to `Example` class. \
If you want to change table, just look for your table in `src/model/tables.py` and do needed changes. \
After creating or updating tables create new migration.

#### Creating migrations
To create new migration simply run
```
alembic revision --autogenerate -m "example comment"
alembic upgrade head
```

#### Linting
We are using following tools:
* black - to run use `make black`
* isort - to run use `make isort`
* pylint - to run use `make pylint`

If you want to lint every file using all at once you can also run `make lint`

#### GitHub Actions
This project uses GitHub Actions for CI. 
The workflow is defined in `.github/workflows/main.yml`. 
It sets up a Python environment, installs the dependencies, runs Docker Compose, and runs the tests.
The workflow is triggered on every push to the `main` branch.

To use GitHub Actions in your repository, you need to add secrets to your repository settings:
- `DB_HOST`
- `DB_USER`
- `DB_PASS`
- `DB_NAME`

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.