FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.toml poetry.lock ./

# Install all dependencies
RUN pip install poetry && poetry install

COPY . ./

# Install the root project
RUN poetry install --only-root

CMD ["poetry", "run", "prod"]
