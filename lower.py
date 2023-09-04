def lower():
    book = 'no doctor'
    book1 = 'NO DENTIST'
    book2 = 'No Therapist'

    print(f'With upper, "{book}" is now "{book.upper()}"')
    print(f'With lower, "{book1}" is now "{book1.lower()}')

    print(f'Book name: "{book}"')
    print(f'Is {book} in upper case? {book.isupper()}')
    print(f'Is {book} in lower case? {book.islower()}')
    print(f'Book name: "{book1}"')
    print(f'Is {book1} in upper case? {book1.isupper()}')
    print(f'Is {book1} in lower case? {book1.islower()}')

    print(f'With casefold,"{book1}" is now "{book1.casefold()}"')

    print(f'With swapcase,"{book2}" is now "{book2.swapcase()}"')
