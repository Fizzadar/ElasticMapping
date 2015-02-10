# ElasticMapping

A simple mapping builder for Elasticsearch.


## Synopsis

```py
from elasticmapping import ElasticMapping
from elasticmapping.types import STRING, INTEGER, FLOAT

# An mapping which forms an ES doc_type
class DocMapping(ElasticMapping):
    __doc_type__ = 'doc_mapping'

    # Top-level attributes
    name = STRING
    ID = INTEGER

    # Nested documents
    nested_document = Nest(
        float_type=FLOAT,
        interger_type=INTEGER
    )

# Print out JSON ready for ES
print DocMapping.json(indent=4)
```

Check out the [full example](./example/mapping.py).


## Types

+ `STRING`
+ `BOOLEAN`
+ `FLOAT`, `DOUBLE`, `INTEGER`, `LONG`, `SHORT`, `BYTE`
+ `DATE` (format = `date`), `DATETIME` (format = `date_hour_minute_second`)


## ElasticQuery support

ElasticMapping can be combined with my other ES library, [ElasticQuery](https://github.com/Fizzadar/ElasticQuery). When ElasticQuery is provided mappings, it limits the fields it can search/aggregate on to that of the mapping - this helps to prevent unexpected errors. For more details see the [query example](./example/query.py). Nested fields are not checked.
