# Hackathon Starter

A simple Python project to get you started with web development and testing using Docker and GitHub Actions.

## Prerequisites

- Python 3.8
- Docker
- Docker Compose

## Getting Started
### Clone the repository

```bash
git clone https://github.com/yourusername/hackathon-starter.git
cd hackathon-starter
```

### Ask for the `.env` file to the project owner, or use postgres default values in the `.env` file:

```bash
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_NAME=postgres
```

### Create a virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Build the Docker image and run the containers

```bash
docker-compose up --build
```

### Testing
```bash
pytest test/api.py  # to test the API
docker exec hackathon-starter_web_1 pytest test/api.py  # to test the database inside the container
```

### Stop the containers

```bash
docker-compose down
```

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
