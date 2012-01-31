# -*- coding: utf-8 -*-

import config


class BaseAppHandler(RequestHandler):

    @property
    def conf(self):
        return config.default

    def get_argument(self, name, default=None, optional=False):
        """
        Overriding Tornado's get_argument() to have None as default
        but also adding the ability to specify an argument as optional,
        so it will not raise an HTTPError needlessly.
        """
        arg = super(BaseAppHandler, self).get_argument(name, default=default)
        if arg is self._ARG_DEFAULT:
            if not optional:
                raise HTTPError(400, "Missing argument %s" % name) # Bad request
            return default
        return arg

    def prepare(self):
        """
        Use "method" as an URL parameter to override the requested
        HTTP method. Necessary in the real-world.
        """
        overriden_method = self.get_argument("method", default=False, optional=True)
        if overriden_method:
            self.request.method = overriden_method