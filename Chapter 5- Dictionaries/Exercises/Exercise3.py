glossary = {
    'string': 'A series of characters.',
    'conditional test': 'A comparison between two values.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'boolean expression': 'An expression that evaluates to True or False.',
    'value': 'An item associated with a key in a dictionary.',
    'float': 'A numerical value with a decimal component.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)