from pydantic import BaseModel


class Context(BaseModel):
    ...


class Command(BaseModel):
    ...

    @classmethod
    def empty(cls) -> 'Command':
        return Command()
