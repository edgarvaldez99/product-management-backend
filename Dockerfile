FROM python:3.11.2-slim-bullseye

ENV PYTHONUNBUFFERED=true
ENV TZ America/Asuncion

WORKDIR /app/

ENV PYTHONPATH=/app

# Install Poetry
RUN apt update && apt install -y curl gettext && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

COPY . /app

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
