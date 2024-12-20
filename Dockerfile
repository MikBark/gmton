FROM python:3.12-slim-bookworm

WORKDIR /app

VOLUME /root/.cache/pip

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY src/ src/

ENTRYPOINT ["python3", "src/main.py"]
