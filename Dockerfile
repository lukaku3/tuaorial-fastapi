FROM python:3.11.9-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true \
  && if [ -f project.toml ]; then poetry install --no-root; fi

ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload" ]
