# ElasticMapping
# File: types.py
# Desc: base Elasticsearch types


class CallableDict(dict):
    def __call__(self, **kwargs):
        new_dict = self.copy()
        new_dict.update(kwargs)
        return new_dict


class Types:
    option_map = {
        'STRING': ['index']
    }

    STRING = CallableDict({
        'type': 'string'
    })

    INTEGER = CallableDict({
        'type': 'integer'
    })

    FLOAT = CallableDict({
        'type': 'integer'
    })

    BOOLEAN = CallableDict({
        'type': 'integer'
    })

    DATE = CallableDict({
        'type': 'date',
        'format': 'date_optional_time'
    })

    DATETIME = CallableDict({
        'type': 'date',
        'format': 'date_hour_minute_second_fraction'
    })
