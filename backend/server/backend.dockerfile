FROM python:3.6

LABEL maintainer="bensong2017@gmail.com"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -i https://pypi.douban.com/simple/ -r /tmp/requirements.txt

COPY ./app/bin/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./app/bin/gunicorn_conf.py /gunicorn_conf.py

COPY ./app/bin/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]