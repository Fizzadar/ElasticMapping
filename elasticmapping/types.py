# ElasticMapping
# File: types.py
# Desc: base Elasticsearch types


class CallableDict(dict):
    BASE = None
    OVERRIDES = None

    def __call__(self, overrides):
        new_dict = CallableDict(self)
        new_dict.OVERRIDES = overrides
        new_dict.BASE = self
        return new_dict


BASE_TYPE = {
    'store': False,
    'doc_values': False
}

STRING = CallableDict({
    'type': 'string',
    'index': 'analyzed'
})

FLOAT = CallableDict({
    'type': 'float'
})

DOUBLE = CallableDict({
    'type': 'double'
})

INTEGER = CallableDict({
    'type': 'integer'
})

LONG = CallableDict({
    'type': 'long'
})

SHORT = CallableDict({
    'type': 'short'
})

BYTE = CallableDict({
    'type': 'byte'
})

BOOLEAN = CallableDict({
    'type': 'boolean'
})

DATE = CallableDict({
    'type': 'date',
    'format': 'date'
})

DATETIME = CallableDict({
    'type': 'date',
    'format': 'date_hour_minute_second'
})


TYPES = {
    name: type
    for name, type in locals().items()
    if isinstance(type, CallableDict)
}
