FROM python:3.9-buster
WORKDIR "/usr/src/app"
COPY poetry.lock .
COPY pyproject.toml .
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN POETRY_VIRTUALENVS_CREATE=false ~/.poetry/bin/poetry install --no-dev

COPY . .

ENTRYPOINT ["python", "run.py"]

