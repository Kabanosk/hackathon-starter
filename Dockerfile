FROM python:3.9-slim-buster

LABEL authors="Wojciech Fiolka <fiolkawojciech@gmail.com>"

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]