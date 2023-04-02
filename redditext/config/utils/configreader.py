import json
import yaml


class JSONConfigReader:
    file = './config/config.json'

    def __init__(self, file='./config/config.json'):
        self.file = file

    def read_config(self):
        with open(self.file, 'r') as config:
            config_data = json.load(config)
            return config_data


class YAMLConfigReader:

    def __init__(self, file='./redditext/config/subs.yml'):
        self.file = file

    def read_config(self):
        with open(self.file, 'r') as config:
            config_data = yaml.load(config)
            return config_data
