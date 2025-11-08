my_dictionary = {
    'name': 'Jack',
    'age': 26,
    'isMale': True
}

my_dictionary = {
    'name': 'John',
    1: [2, 4, 3]
}

print(my_dictionary['name'])

my_dictionary['address'] = 'Downtown'

my_dictionary.pop('name')

print("Address :", my_dictionary.get('address'))