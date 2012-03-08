# -*- coding: utf-8 -*-

import config

from tornado.web import HTTPError, RequestHandler


class BaseAppHandler(RequestHandler):

    @property
    def conf(self):
        return config.default

    def get_argument(self, name, default=None, required=False):
        """
        Overriding Tornado's get_argument() to consider an argument optional
        by default and return None if it's not present.
        """
        arg = super(BaseAppHandler, self).get_argument(name, default=default)
        if arg is default and required:
            raise HTTPError(400, "Missing argument %s" % name) # Bad request
        return arg

    def prepare(self):

        # use "method" as an URL param to overwrite the HTTP method
        overriden_method = self.get_argument("method", default=False)
        if overriden_method:
            self.request.method = overriden_method
