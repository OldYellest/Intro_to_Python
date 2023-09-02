def exin():
    books = ['Concrete Hell', 'No Doctor', 'Sniper Hide']
    movies = ['RED', 'Cobweb', 'Dark Knight']
    numbers = range(12)
    a_string = 'Little Red Riding-Hood comes to me one Christmas Eve to give me information of the cruelty and ' \
               'treachery of that dissembling Wolf who ate her grandmother. '

    print(f'Books: {books}')
    print(f'Movies: {movies}')
    print(f'Numbers: {numbers}')
    print(f'Story: {a_string}')

    print(f"""Red is in the story: {'Red' in a_string}""")

    # Checks to see if it contains the word "red"

    print(f"""'No Dentist' is not in the books list: {'No Dentist' not in books}""")
    print(f"""'RED' is not in the movies list: {'RED' not in movies}""")
    print(f"""16 is not in the numbers list: {16 not in numbers}""")

    # use of 'not' to find if string does not have object
