from typing import Protocol

import httpx

from models import Command, Context


class Api(Protocol):

    def post(self, command: Command) -> Context:
        pass


class SimpleApi:

    def __init__(self, client: httpx.Client, post_url: str) -> None:
        self._client = client
        self._post_url = post_url

    def post(self, body: Command) -> Context:
        resp = self._client.post(
            url=self._post_url,
            json=body.model_dump_json(),
        )
        return Context(**resp.json())
