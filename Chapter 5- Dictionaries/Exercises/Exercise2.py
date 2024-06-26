glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

words = ['string', 'comment', 'list', 'loop', 'dictionary']

for word in words:
    print("\n" + word.title() + ": " + glossary[word])