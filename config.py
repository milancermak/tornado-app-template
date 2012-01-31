# -*- coding: utf-8 -*-
"""
List of configuration variables and enumerations used throughout the app.
"""

import os


_kv = {
    "cookie_secret": "foo",
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}


class AppConfig:
    """
    Class holding all configurations necessary for the app to run.

    The values are accessible as attributes of an instance of this class.
    When you access an attribute, its value is at first looked up in the
    enviroment variables (key is uppercased). If it is not found there,
    the class checks a config dictionary passed to it at init. If the value
    is not even there, it returns None.
    """

    def __init__(self, config_dict):
        self.vals = config_dict

    def __getattr__(self, name):
        """
        Get the value from the ENV, if it's not present, get
        it from the dictionary. Returns None if not found.
        """
        return os.environ.get(name.upper(), self.vals.get(name.lower()))

default = AppConfig(_kv)
