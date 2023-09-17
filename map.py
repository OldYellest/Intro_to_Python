# Mapping type is useful for storing data in key value pairs

def books():
    catalog = {
        'C Programming Language': 35,
        'Intro to Algorithms': 100,
        'Clean Code: Agile Software Craftsmanship': 50
    }

    print(catalog)

    cpl = 'C Programming Language'
    algo = 'Intro to Algorithms'

    print(f"The price of {cpl} is ${catalog.get(cpl)}")
    print(f"The price of {algo} is ${catalog.get(algo)}")

    print('\nWe will now increase the price of the first book and add a new one.')

    catalog[cpl] = 45
    catalog['How to Code 101'] = 35

    print(catalog)

    print('\nWe will now remove an item, but not value, and remove both item and value')

    print(catalog.popitem())  # This removes the last item and returns that as a tuple
    print(catalog.pop(cpl))  # This returns value of given key and removes pair
    print(catalog)

    print('\nWe will now wipe the whole selection')
    catalog.clear()
    print(catalog)


# the list is a mapping type known as dictionary
# similar to list or tuple, but use {} instead of () or []
# strings on left are keys, numbers are the values
# gain access to keys using get()
# dictionaries are mutable, can add, remove, and change existing items
# removing items needs the popitem() or pop() function

def view():
    book = {
        'C Programming Language': 35,
        'Intro to Algorithms': 100,
        'Clean Code: Agile Software Craftsmanship': 50
    }

    print(book)
    print("\nThe following returns the keys: ")
    for key in book.keys():
        print(key)

# keys() returns the keys of a dictionary and can be looped over

    print("\nThe following returns the values: ")
    for value in book.values():
        print(value)

# values() returns the values in a dictionary

    print("\nThe following returns both keys and values: ")
    for item in book.items():
        print(item)

# items() returns both keys and values and tuples