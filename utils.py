# -*- coding: utf-8 -*-

import json
import re
import uuid

import times

from tornado.web import HTTPError


def check_valid_email(email_string):
    """ Tests a string against an email validation regexp and returns a boolean """

    # Attribution for the regexp: http://axonflux.com/handy-a-regex-that-validates-all-valid-email
    email_pattern = re.compile("^([\w\!\#$\%\&\'\*\+\-\/\=\?\^\`{\|\}\~]+\.)*[\w\!\#$\%\&\'\*\+\-\/\=\?\^\`{\|\}\~]+@((((([a-z0-9]{1}[a-z0-9\-]{0,62}[a-z0-9]{1})|[a-z])\.)+[a-z]{2,6})|(\d{1,3}\.){3}\d{1,3}(\:\d{1,5})?)$")
    return not not email_pattern.match(email_string)

def ensure(expression_result, fail_msg=None, status=500):
    """
    Raises an HTTP 500 if the expression result is not True,
    with an optional failure message.
    Used as a non-debug substitute for assert
    """
    if not expression_result:
        raise HTTPError(status, fail_msg if fail_msg else "Operation failed")

def iso_utc_now():
    """ Return the current date and time in UTC timezone in ISO 8601 format """
    return times.format(times.now(), "UTC")

def to_iso_utc(iso_string):
    """ Return the UTC representation of a ISO 8601 timestamp """
    return times.format(times.to_universal(iso_string), "UTC")
