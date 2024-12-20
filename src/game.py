from api import Api
from logic import Logic
from models import Command


class Game:

    def __init__(self, api: Api, logic: Logic) -> None:
        self._api = api
        self._logic = logic

    def play(self) -> None:
        context = self._api.post(Command.empty())
        while True:
            command = self._logic.solve(context)
            context = self._api.post(command)
