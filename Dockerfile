FROM python:3.9
WORKDIR "/usr/src/app"
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev

COPY . .

ENTRYPOINT ["python", "run.py"]

