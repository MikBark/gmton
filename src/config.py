import json
from typing import Any

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServiceConfig(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)

    post_url: str
    token: str = Field(validation_alias='API_TOKEN')

    @computed_field
    def client_config(self) -> dict[str, Any]:
        return {
            'headers': {'X-API-Key': self._token},
        }


def read_json(path: str) -> dict[str, Any]:
    with open(path, 'r') as rf:
        return json.load(rf)


service_config = ServiceConfig()
logic_config = read_json('conf/logic.json')
