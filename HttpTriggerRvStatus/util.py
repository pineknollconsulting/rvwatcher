from datetime import datetime
from math import ceil


def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')


def datetime_to_epoch(time):
    """
    Converts a given datetime object to an epoch timestamp
    @param - time

    Returns int
    """
    diff = time - datetime.utcfromtimestamp(0)
    return int(ceil(diff.total_seconds()))
