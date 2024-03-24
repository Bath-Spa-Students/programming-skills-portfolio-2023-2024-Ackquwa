rivers = { 
    'mississippi': 'united states', 
    'kuskokwim': 'alaska',
    'nile': 'egypt',
    'yangtze': 'china',
    'fraser': 'canada',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThese rivers are included in this data set:")

for river in rivers.keys():
    print("- " + river.title())

print("\nThese countries are included in this data set:")

for country in rivers.values():
    print("- " + country.title())