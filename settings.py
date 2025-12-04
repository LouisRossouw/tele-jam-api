import os
from lib.utils import read_json, write_to_json


class Settings():
    def __init__(self):
        self.root_path = os.path.dirname(__file__)

        self.bot_config_path = os.path.join(self.root_path, "configs", "bots.json")  # nopep8
        self.bots_config = read_json(self.bot_config_path)

        self.config_path = os.path.join(self.root_path, "configs", "config.json")  # nopep8
        self.config = read_json(self.config_path)

        self.manifest = os.path.join(self.root_path, "data", "manifest.json")  # nopep8

        self.host = self.config.get('host')
        self.port = self.config.get('port')

        self.notifications = self.config.get('notifications')

    def get_bot_config(self):
        """ Returns the bog config and a json object """
        return read_json(self.bot_config_path)

    def get_config(self):
        """ Returns the config and a json object """
        return read_json(self.config_path)

    def update_config(self, data):
        """ Updates and writes to the config """
        return write_to_json(self.config_path, data)

    def get_setting(self, key):
        """ Returns a key value from the config """
        return read_json(self.config_path).get(key)
