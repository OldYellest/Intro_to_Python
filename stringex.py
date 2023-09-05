def excount():
    paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of 
    Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in 
    the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to 
    welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved, 
    ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer, 
    a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal 
    officer.'''

    substring = 'morning'

    print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')

def saw():
    string = 'The brown dog jumped over the lazy red fox'
    string1 = 'The,brown,dog,jumped,over,the,lazy,red,fox'

    word_list = string.split()
    word_list1 = string1.split(',', 5)

    print(string)
    print(f'With split, it now reads:"{word_list}"')
    print(string1)
    print(f'With split and parameters, it now reads:"{word_list1}"')

def glue():
    words = ['The', 'brown', 'dog', 'jumped', 'over', 'the', 'lazy', 'red', 'fox']
    words1 = ['The ', 'brown ', 'dog ', 'jumped ', 'over ', 'the ', 'lazy ', 'red ', 'fox ']
    string = ''

    string = string.join(words)

    print(words)
    print(f'With join, it now reads: {string}')
    string = ''

    string = string.join(words1)

    print(words1)
    print(f'With join and spaces, it now reads: {string}')


