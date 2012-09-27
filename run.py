# -*- coding: utf-8 -*-

import argparse
import locale

import tornado.ioloop
import tornado.web

import config
from config import AppConfig
import routes

# date of release; run fab timestamp to set it
__date__ = "2012-03-01 19:02:03+0000"
__version__ = "1"

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-p", "--port", type=int)
    clargs = vars(args_parser.parse_args())
    port = clargs["port"]
    if port is None:
        port = 8000

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    application = tornado.web.Application(routes.all,
                                          cookie_secret=AppConfig.default().cookie_secret,
                                          debug=config.is_debug())
    application.listen(port, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
