import httpx

from api import SimpleApi
from config import logic_config, service_config
from game import Game
from logic import EmptyLogic

if __name__ == '__main__':
    game = Game(
        SimpleApi(
            httpx.Client(
                transport=httpx.HTTPTransport(**service_config.transport_config),
                **service_config.client_config,
            ),
            service_config.post_url,
        ),
        EmptyLogic(**logic_config),
    )
    game.play()
