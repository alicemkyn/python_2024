'''
JavaScript Object Notation

---JSON == Python---
- object == dict
- array == list
- string == str
- number(int) == int
- number(real) == float
- true == True
- false == False
- null == None

dump(s)- s means string (dict to JSON str)
dump - will dump JSON str to a file.json
load(s)- s means string (JSON str to dict)
load - will load JSON str from a file.json
'''

import json

people_string: str = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["john@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''


########### json.loads() method to convert JSON str to dict ############
data = json.loads(people_string)

print(type(data)) # <class 'dict'>
print(data) # {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['john@bogusemail.com', 'john.smith@work-place.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'has_license': True}]}
for person in data['people']:
    print(person['name'])



########### json.dumps() method to convert dict to JSON str ############
# lets delete people phone key,vals.And convert it back into JSON str.
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True) 
# Every level indents 2 steps deeper
# All the keys will be sorted alphabetically

print(type(new_string)) #<class 'str'>
print(new_string)
'''
Output:
{
  "people": [
    {
      "emails": [
        "john@bogusemail.com",
        "john.smith@work-place.com"
      ],
      "has_license": false,
      "name": "John Smith"
    },
    {
      "emails": null,
      "has_license": true,
      "name": "Jane Doe"
    }
  ]
}
'''

############## json.load method to load a data from file ###############
with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])



############# json.dump method to dump the data to a file ##############
#lets remove the area codes from data and dump it in a new file
for state in data['states']:
    del state['area_codes']
    
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)

