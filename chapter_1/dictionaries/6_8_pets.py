pets = []

pet = {
    'type_of_pet': "dog",
    'owner': 'giannis'
}

pets.append(pet)

pet = {
    'type_of_pet': "cat",
    'owner': 'spiros'
}

pets.append(pet)

pet = {
    'type_of_pet': "hamster",
    'owner': 'panos'
}

pets.append(pet)

for pet in pets:
    print(f"{pet['owner'].title()} is the owner of a {pet['type_of_pet']}")