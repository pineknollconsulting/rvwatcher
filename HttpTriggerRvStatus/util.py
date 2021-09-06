from datetime import datetime
from math import ceil
import re


class CamelToSnakeConverter(object):
    pattern1 = re.compile('(.)([A-Z][a-z]+)')
    pattern2 = re.compile('([a-z0-9])([A-Z])')

    @classmethod
    def convert(cls, name: str) -> str:
        name = cls.pattern1.sub(r'\1_\2', name)
        return cls.pattern2.sub(r'\1_\2', name).lower()


def camel_to_snake(name: str):
    return CamelToSnakeConverter.convert(name)


def datetime_to_epoch(time):
    """
    Converts a given datetime object to an epoch timestamp
    @param - time

    Returns int
    """
    diff = time - datetime.utcfromtimestamp(0)
    return int(ceil(diff.total_seconds()))
