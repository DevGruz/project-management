FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . .

# CMD ["sh", "-c", "alembic upgrade head && python app/main.py"]

CMD ["sh", "-c", "python app/main.py"]