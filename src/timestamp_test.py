# -*- coding: utf-8 -*-
__author__ = 'leo'
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) YEAR by AUTHOR.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from datetime import datetime
import calendar
import time


def local_to_utc(date_value):
    utc_timetuple = datetime.strptime(date_value, '%Y/%m/%d %H:%M:%S').timetuple()
    ts = calendar.timegm(utc_timetuple)
    return ts * 1000


def local_timestamp(date_value):
    utc_timetuple = datetime.strptime(date_value, '%Y/%m/%d %H:%M:%S').timetuple()
    ts = time.mktime(utc_timetuple)
    return int(ts) * 1000


date_str = '2015/10/27 00:00:00'
print local_to_utc(date_str)
print local_timestamp(date_str)
