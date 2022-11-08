#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#
#WORKDIR /app/
#
## Install Poetry
#RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false
#
## Copy poetry.lock* in case it doesn't exist in the repo
#COPY ./app/pyproject.toml ./app/poetry.lock* /app/
#
## Allow installing dev dependencies to run tests
#ARG INSTALL_DEV=false
#RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"
#
## For development, Jupyter remote kernel, Hydrogen
## Using inside the container:
## jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
#ARG INSTALL_JUPYTER=false
#RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"
#
#COPY ./app /app
#ENV PYTHONPATH=/app

FROM python:3.9-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./bin/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./bin/gunicorn_conf.py /gunicorn_conf.py

COPY ./bin/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]