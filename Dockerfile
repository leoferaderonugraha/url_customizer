from python:3.9

WORKDIR /code/
EXPOSE 1405

# opt for mount
# COPY . .

# RUN pip install poetry
# RUN poetry install &&
#    poetry run alembic upgrade head

# ENTRYPOINT ["poetry", "run", "flask", "run"]
