# -*- coding: utf-8 -*-

import argparse

import tornado.ioloop
import tornado.web

import config
import routes

# date of release; run fab timestamp to set it
__date__ = "2012-01-31 23:21:31"
__version__ = "1"

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-p", "--port", type=int)
    clargs = vars(args_parser.parse_args())
    port = clargs["port"]
    if port is None:
        port = 8000

    application = tornado.web.Application(routes.all,
                                          cookie_secret=config.default.cookie_secret,
                                          debug=config.default.debug)
    application.listen(port, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
