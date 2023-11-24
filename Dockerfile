FROM python:3.9.18-slim-bullseye

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt


COPY setup.cfg /app/
COPY pyproject.toml /app/
COPY setup.py /app/
COPY src /app/src

RUN pip install .

EXPOSE 5000

ENTRYPOINT [ "todo_api" ]




