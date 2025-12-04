import os

from settings import Settings


class Bot:
    def __init__(self, bot_name):
        self.settings = Settings()

        bots_config = self.settings.get_bot_config()
        self.bot_config = bots_config[bot_name]

        env_key = self.bot_config.get('env_key')

        self.token = os.getenv(env_key)
        self.active = self.bot_config.get('active')
        self.label = self.bot_config.get('label')
