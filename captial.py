from string import capwords
def capital():
    state = 'kentucky'
    country = 'United States'
    book1 = "george's stump"
    book2 = 'concrete hell'
    address = 'apartment 23, road 01, nowhere'

    print(f'Capitalize makes {state} into {state.capitalize()}.')
    print(f'Capitalize makes {country} into {country.capitalize()}, but not both words.')
    print(f'Title makes {country} into {country.title()}.')
    print(f'Title makes {book1} into {book1.title()}, but messes up with the apostrophe.')
    print(f'Capwords makes {book1} into {capwords(book1)}.')
    print(f"Capwords makes {address} into {capwords(address, ', ')}, using a custom delimiter.")
    print(f'Is "{book2}" in title case? {book2.istitle()}')
    print(f'Is "{book2.title()}" in title case? {book2.title().istitle()}')

