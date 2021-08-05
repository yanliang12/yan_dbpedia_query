import yan_dbpedia_query

'''

import yan_entity_linking

entity_linking_results = yan_entity_linking.entity_linking("San Francisco and San Jose")

for e in entity_linking_results:
	print(e)

query_wikipage_ids = [e['entity_wikipage_id'] for e in entity_linking_results]

print(query_wikipage_ids)


query_wikipage_ids = [
"5407",
"856",
"3956428",
"5405",
"18950756",
]

query_wikipage_ids = ['18603746', '27643', '5405']
query_wikipage_ids = ['18603746', '27643']
query_wikipage_ids = ['7529378', '856']

'''

query_wikipage_ids = ['49728', '53446']

###

triplets = yan_dbpedia_query.find_triplets_of_entities(
	query_wikipage_ids,
	skip_rdf_schema_relation = False,
	)

for e in triplets:
	t = '(%s,%d)-[%s]->(%s,%d)'%(
		e['subject_name'],
		e['subject_out_degree'],
		e['relation'],
		e['object_name'],
		e['object_out_degree'],
		)
	print(t)

###

top_common_subject_object_tripltes = yan_dbpedia_query.find_top_common_subject_object_of_entity_pairs(
	query_wikipage_ids,
	triplets,
	top_triplet_number = 2,
	)

for e in top_common_subject_object_tripltes:
	t = '(%s,%d)-[%s]->(%s,%d)'%(
		e['subject_name'],
		e['subject_out_degree'],
		e['relation'],
		e['object_name'],
		e['object_out_degree'],
		)
	print(t)

###

top_subject_object_triplets = yan_dbpedia_query.find_top_subject_object_for_each_entity(
	query_wikipage_ids,
	triplets,
	top_triplet_number = 2
	)

for e in top_subject_object_triplets:
	t = '(%s,%d)-[%s]->(%s,%d)'%(
		e['subject_name'],
		e['subject_out_degree'],
		e['relation'],
		e['object_name'],
		e['object_out_degree'],
		)
	print(t)

###

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

