# -*- coding: utf-8 -*-
"""
List of configuration variables and enumerations used throughout the app.
"""

import os


class AppConfig(object):

    """
    Class holding all configurations necessary for the app to run.

    The values are accessible as attributes of an instance of this class.
    When you access an attribute, its value is at first looked up in the
    enviroment variables (key is uppercased). If it is not found there,
    the class checks a config dictionary passed to it at init. If the value
    is not even there, it returns None.
    """

    CFG = {
        "cookie_secret": "foo",
        "server_realm": "dev",
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }

    def __getattr__(self, name):
        """
        Get the value from the ENV, if it's not present, get
        it from the dictionary. Returns None if not found.
        """
        return os.environ.get(name.upper(), self.CFG.get(name.lower()))

    @staticmethod
    def default():
        if not hasattr(AppConfig, "_default"):
            AppConfig._default = AppConfig()
        return AppConfig._default

def is_debug():
    return AppConfig.default().server_realm != "live"
