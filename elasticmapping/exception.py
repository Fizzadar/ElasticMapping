# ElasticMapping
# File: exception.py
# Desc: ElasticMapping exceptions


# A base exception
class ElasticMappingException(Exception):
    pass

class NoESClient(ElasticMappingException):
    pass

class NoDocType(ElasticMappingException):
    pass

class NoIndexName(ElasticMappingException):
    pass

class NoElasticQuery(ElasticMappingException):
    pass
