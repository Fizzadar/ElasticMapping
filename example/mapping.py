# ElasticMapping
# File: example/mapping.py
# Desc: example mapping file w/ commands

from elasticsearch import Elasticsearch
from elasticmapping import ElasticMapping, Nest
from elasticmapping.types import STRING, DATETIME, FLOAT, INTEGER


# A base mapping
class BaseMapping(ElasticMapping):
    __es__ = Elasticsearch()
    __index__ = 'mapping_test'

    # Override all string attributes
    __STRING__ = {
        'index': 'not_analyzed'
    }

    # Example fields
    slug = STRING
    datetime = DATETIME({
        'format': 'date_hour_minute_second_fraction'
    })


# An mapping which forms an ES doc_type
class DocMapping(BaseMapping):
    __doc_type__ = 'doc_mapping'

    # Overrides the BaseMapping __STRING__ override
    name = STRING({
        'index': 'analyzed'
    })

    # Nested documents
    nested_document = Nest(
        float_type=FLOAT,
        interger_type=INTEGER
    )


# Print out JSON ready for ES
print DocMapping.json(indent=4)

# Create the mappings with provided __es__ client
print DocMapping.put()
