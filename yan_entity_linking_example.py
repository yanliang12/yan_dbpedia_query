#######yan_entity_linking_example.py########

import yan_entity_linking

o = yan_entity_linking.entity_linking("I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997")

for e in o:
	print(e)

'''

{'mention': 'heriot watt university dubai', 'entity_wikipage_id': '3956428', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997'}
{'mention': 'china', 'entity_wikipage_id': '5405', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997'}
{'mention': 'abu dhabi', 'entity_wikipage_id': '18950756', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997'}
{'mention': 'apple', 'entity_wikipage_id': '856', 'sentence': 'I study at Heriot-Watt University Dubai, but I live at Abu Dhabi. I want to work at Apple. I was born in China, 1997'}

''' 
#######yan_entity_linking_example.py########