# yan_dbpedia_query

```bash
docker pull yanliang12/yan_dbpedia_query:1.0.2
```

example

```python
import yan_dbpedia_query

query_wikipage_ids = ['49728', '53446']

triplets = yan_dbpedia_query.find_triplets_of_entities(
	query_wikipage_ids,
	skip_rdf_schema_relation = False,
	)

top_between_relation_tripltes = yan_dbpedia_query.find_top_relations_between_entity_pairs(
	query_wikipage_ids,
	triplets,
	top_triplet_number = 2,
	)

for e in top_between_relation_tripltes:
	t = '(%s,%d)-[%s]->(%s,%d)'%(
		e['subject_name'],
		e['subject_out_degree'],
		e['relation'],
		e['object_name'],
		e['object_out_degree'],
		)
	print(t)
```
