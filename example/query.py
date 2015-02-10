# ElasticMapping
# File: example/query.py
# Desc: example mapping file w/ ElasticQuery extensions

from elasticquery import Filter

from mapping import DocMapping


q = DocMapping.query.must(
    Filter.term(slug='test_slug'),
    Filter.nested('nested_document', must=[
        Filter.term(float_type=1.0)
    ])
)
q.must_not(
    Filter.term(name='Test Name')
)


if __name__ == '__main__':
    # Print out JSON ready for ES
    print 'JSON', q.json(indent=4)

    # Get the results with provided __es__ client
    print 'GET', q.get()
