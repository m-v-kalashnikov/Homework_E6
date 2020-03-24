import json
from pymemcache.client import base


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))
    raise Exception("Unknown serialization format")


client = base.Client(('localhost', 11211),
                     serializer=json_serializer,
                     deserializer=json_deserializer)
