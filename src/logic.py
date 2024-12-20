from typing import Protocol

from models import Command, Context


class Logic(Protocol):

    def solve(self, context: Context) -> Command:
        pass


class EmptyLogic:

    def __init__(self, field: str) -> None:
        self._field = field

    def solve(self, context: Context) -> Command:
        return Command.empty()
