# ElasticMapping
# File: mapping.py
# Desc: a very simple Elasticsearch mappings manager

import json

from .types import Types


class ElasticMapping(object):
    MAPPINGS = None

    def __init__(self, doc_values=True, store=True, **kwargs):
        global_kwargs = {
            'doc_values': doc_values,
            'store': store
        }

        # Apply global defaults for all types
        types = [type for type in dir(Types) if type.isupper()]
        for type in types:
            getattr(Types, type).update(global_kwargs)

        # Apply per-type options from kwargs
        for type, options in Types.option_map.iteritems():
            for option_key in options:
                if kwargs.get(option_key):
                    getattr(Types, type)[option_key] = kwargs[option_key]

    def __getattr__(self, name):
        '''Allows us to ElasticMapping.STRING'''
        return getattr(Types, name)

    def nest(self, fields):
        '''Nests a set of fields'''
        return {
            'type': 'nested',
            'properties': fields
        }

    def create(self, doc_type, fields, dynamic=False):
        '''Builds a mapping which can be sent to ES'''
        self.MAPPINGS = {
            doc_type: {
                'dynamic': dynamic,
                'properties': fields
            }
        }

    def cli(self):
        import .cli
