# Hackathon Starter

A simple Python project to get you started with web development and testing using Docker and GitHub Actions.

## Prerequisites

- Python 3.8
- Docker
- Docker Compose
- Poetry

## Getting Started
### Clone the repository

```bash
git clone https://github.com/yourusername/hackathon-starter.git
cd hackathon-starter
```

### Ask for the `.env` file to the project owner, or use postgres default values in the `.env` file:

```bash
DB_USER=postgres
DB_PASS=postgres
DB_HOST=db
DB_NAME=postgres
DB_PORT=5432
```

### Create a virtual environment and install the dependencies

```bash
poetry shell 
```

### Build the Docker image and run the containers

```bash
docker-compose up --build
```

### Testing
```bash
pytest test/test_api.py  # to test the API
docker exec hackathon-starter_web_1 poetry run pytest tests/test_database.py  # to test the database inside the container
```

### Stop the containers

```bash
docker-compose down
```

### Creating or updating tables in database
To create new table in database just create needed class in `src/model/tables.py` similar to `Example` class.
If you want to change table, just look for your table in `src/model/tables.py` and do needed changes.
After creating or updating tables create new migration.

### Creating migrations
To create new migration simply run
```
alembic revision --autogenerate -m "example comment"
alembic upgrade head
```

### Linting
We are using following tools:
* black - to run use `black <path to file>`
* isort - to run use `isort <path to file>`

### GitHub Actions
This project uses GitHub Actions for CI. 
The workflow is defined in `.github/workflows/main.yml`. 
It sets up a Python environment, installs the dependencies, runs Docker Compose, and runs the tests.
The workflow is triggered on every push to the `main` branch.

To use GitHub Actions in your repository, you need to add secrets to your repository settings:
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.