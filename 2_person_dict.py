person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person['children'])

print(type(person['children']))

print(person['children'][1])

print(person['pets']['cat'])


for child_name in person['children']:
    print(child_name)

for pet_name in person['pets']:
    print(person['pets'][pet_name])