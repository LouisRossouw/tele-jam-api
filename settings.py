import os
from lib.utils import read_json, write_to_json


class Settings():
    def __init__(self):
        self.root_path = os.path.dirname(__file__)

        self.config_path = os.path.join(self.root_path, "configs", "config.json")  # nopep8
        self.config = read_json(self.config_path)

    def get_config(self):
        """ Returns the config and a json object """
        return read_json(self.config_path)

    def update_config(self, data):
        """ Updates and writes to the config 
        :param data: dict 
        """
        return write_to_json(self.config_path, data)

    def get_setting(self, key):
        """ Returns a key value from the config 
        :param key: string - ex: {key: value}
        """

        data = read_json(self.config_path)
        return data.get(key)
