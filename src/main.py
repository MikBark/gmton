from httpx import Client

from api import Api
from config import logic_config, service_config
from game import Game
from logic import Logic

if __name__ == '__main__':
    game = Game(
        Api(Client(**service_config.client_config), service_config.post_url),
        Logic(**logic_config),
    )
    game.play()
