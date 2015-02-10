# ElasticMapping
# File: mapping.py
# Desc: a very simple Elasticsearch mappings builder

import json

try:
    from elasticquery import ElasticQuery
except ImportError:
    ElasticQuery = None

from .types import TYPES, CallableDict
from .exception import NoESClient, NoDocType, NoIndexName, NoElasticQuery


class Nest(object):
    '''A nested ES mapping'''
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

class ElasticMappingMeta(type):
    '''Metaclass to provide a @classproperty for the query attribute'''
    @property
    def query(cls):
        if cls._query is not None:
            return cls._query

        if ElasticQuery is None:
            raise NoElasticQuery()

        if cls.__es__ is None:
            raise NoESClient()
        if cls.__index__ is None:
            raise NoIndexName()
        if cls.__doc_type__ is None:
            raise NoDocType()

        query = ElasticQuery(
            es=cls.__es__,
            index=cls.__index__,
            doc_type=cls.__doc_type__,
            mapping=cls.attributes()
        )

        cls._query = query
        return query

class ElasticMapping(object):
    '''A class for building ES mappngs'''
    __metaclass__ = ElasticMappingMeta

    __es__ = None
    __index__ = None
    __doc_type__ = None

    # Dynamic: false by default
    __dynamic__ = False

    # Cache
    _attributes = None
    _query = None

    @classmethod
    def attributes(cls):
        '''Builds an internal representation of the mapping, with no top-level nesting ES uses'''
        if cls._attributes is not None:
            return cls._attributes

        def parse_attributes(object):
            out = {}
            for name in dir(object):
                attribute = getattr(object, name)

                # We are some kind of type
                if isinstance(attribute, CallableDict):
                    attribute_base = getattr(attribute, 'BASE')

                    type_name = None
                    for type_name, type in TYPES.iteritems():
                        if attribute is type or attribute_base is type:
                            break

                    # Override with any __<type_name>__ attributes on this class
                    class_override_name = '__{}__'.format(type_name)
                    class_overrides = getattr(cls, class_override_name, None)
                    if class_overrides is not None:
                        attribute.update(class_overrides)

                    # Override with attribute.OVERRIDES
                    attribute_overrides = getattr(attribute, 'OVERRIDES')
                    if attribute_overrides is not None:
                        attribute.update(attribute_overrides)

                    out[name] = attribute

                # We are a nested document
                elif isinstance(attribute, Nest):
                    out[name] = {
                        'type': 'nested',
                        'properties': parse_attributes(attribute)
                    }

            return out

        out = parse_attributes(cls)

        cls._attributes = out
        return out

    @classmethod
    def dict(cls):
        '''Nests the internal attributes dict inside the doc_type/etc ES format'''
        if cls.__doc_type__ is None:
            raise NoDocType()

        return {
            cls.__doc_type__: {
                'dynamic': cls.__dynamic__,
                'properties': cls.attributes()
            }
        }

    @classmethod
    def json(cls, indent=None):
        '''JSON version of .dict()'''
        return json.dumps(
            cls.dict(), indent=indent
        )

    @classmethod
    def put(cls):
        '''Puts the mapping to ES when __es__ and __index__ are provided to the class'''
        if cls.__es__ is None:
            raise NoESClient()
        if cls.__index__ is None:
            raise NoIndexName()
        if cls.__doc_type__ is None:
            raise NoDocType()

        return cls.__es__.indices.put_mapping(
            index=cls.__index__,
            doc_type=cls.__doc_type__,
            body=cls.dict()
        )
