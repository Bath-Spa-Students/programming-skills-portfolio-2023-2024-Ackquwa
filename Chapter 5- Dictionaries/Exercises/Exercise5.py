pets = []

pet = {
    'animal type': 'python',
    'name': 'pablo',
    'owner': 'guittierez',
    'weight': 18,
    'eats': 'rodents',
}

pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'kafka',
    'owner': 'stelle',
    'weight': 4,
    'eats': 'seeds',
}

pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'sampo',
    'owner': 'hanabi',
    'weight': 25,
    'eats': 'dreams',
}

pets.append(pet)

for pet in pets:
    print("\nHere's what I know about this pet named " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))