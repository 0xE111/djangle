FROM python:3.10-slim
EXPOSE 8000
WORKDIR /root

# TODO: 2-stage build

RUN apt-get update && apt-get install -y gcc git && pip install gunicorn

COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir wheel -r /tmp/requirements.txt

COPY src ./
CMD ["./entrypoint.sh"]
