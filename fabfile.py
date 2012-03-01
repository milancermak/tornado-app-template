# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.context_managers import hide

from utils import iso_utc_now

@task
def timestamp():
    """ Update the __date__ field in run.py """

    timestamp = iso_utc_now()
    with hide("running"):
        local("sed -E -e 's/(__date__[[:space:]]+=[[:space:]]+\")([[:digit:]]{4}-[[:digit:]]{2}-[[:digit:]]{2} [[:digit:]]{2}:[[:digit:]]{2}:[[:digit:]]{2}\+[[:digit:]]{4})\"/\\1%s\"/' -i .tmp run.py" % timestamp)
        local("rm run.py.tmp")
