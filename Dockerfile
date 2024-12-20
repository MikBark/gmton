FROM python:3.12-slim-bookworm

ARG REPO_URL=https://github.com/MikBark/gmton
ARG BRANCH=master

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --branch ${BRANCH} ${REPO_URL} .

VOLUME /root/.cache/pip

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

ENTRYPOINT ["python3", "src/main.py"]
