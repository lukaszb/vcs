"""
This module provides some useful tools for ``vcs`` like annotate/diff html
output. It also includes some internal helpers.
"""
import sys
import time
import datetime


def makedate():
    lt = time.localtime()
    if lt[8] == 1 and time.daylight:
        tz = time.altzone
    else:
        tz = time.timezone
    return time.mktime(lt), tz


def date_fromtimestamp(unixts, tzoffset=0):
    """
    Makes a datetime objec out of unix timestamp with given timezone offset
    :param unixts:
    :param tzoffset:
    """
    return datetime.datetime(*time.gmtime(float(unixts) - tzoffset)[:6])


def safe_unicode(s):
    """
    safe unicode function. In case of UnicodeDecode error we try to return
    unicode with errors replace, if this fails we return unicode with
    string_escape decoding
    """

    try:
        u_str = unicode(s)
    except UnicodeDecodeError:
        try:
            u_str = unicode(s, 'utf-8', 'replace')
        except UnicodeDecodeError:
            # In case we have a decode error just represent as byte string
            u_str = unicode(str(s).encode('string_escape'))

    return u_str

if sys.version_info >= (2, 7):
    unittest = __import__('unittest')
else:
    unittest = __import__('unittest2')

