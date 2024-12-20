FROM python:3.12-slim-bookworm

ARG REPO_URL=https://github.com/MikBark/gmton
ARG BRANCH=master

VOLUME /root/.cache/pip,/var/cache/apt

WORKDIR /app

RUN --mount=type=cache,target=/var/cache/apt apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --branch ${BRANCH} ${REPO_URL} .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

CMD ["python3", "src/main.py"]
