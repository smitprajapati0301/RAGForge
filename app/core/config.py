"""
Loads project configuration from config.yaml.
"""

from pathlib import Path

import yaml


class Config:

    def __init__(self):

        config_path = Path("configs/config.yaml")

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self):
        return self.config


config = Config().get()