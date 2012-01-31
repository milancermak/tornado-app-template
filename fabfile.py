# -*- coding: utf-8 -*-

import datetime

from fabric.api import *
from fabric.context_managers import hide


@task
def timestamp():
    """ Update the __date__ field in app.py """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z")
    with hide("running"):
        local("sed -E -e 's/(__date__[[:space:]]+=[[:space:]]+\")([[:digit:]]{4}-[[:digit:]]{2}-[[:digit:]]{2} [[:digit:]]{2}:[[:digit:]]{2}:[[:digit:]]{2})\"/\\1%s\"/' -i .tmp app.py" % timestamp)
        local("rm app.py.tmp")
