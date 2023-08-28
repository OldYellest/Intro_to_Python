from inputs import inputs
from list import lists
from numbers import num
from variables import var
from range import ex1range, ex2range
from index import exindex
from for_while import exfor, exwhile, exloop, whileloop

# from and imports only 'activate' once given function in script that refrences it
# Otherwise, function causes error

def main():
    print('Hello, World!!!')

def programs():
    program = ("for_while", "index", "inputs", 'list', 'main', 'numbers', 'range', 'variables')
    print(program)
    choice = input(f'Select a program from the list above: ')

    if choice == "for_while":
        c1r = input(f'Choose: exfor, exwhile, exloop, whileloop: ')
        if c1r == "exfor":
            exfor()
        if c1r == "exwhile":
            exwhile()
        if c1r == "exloop":
            exloop()
        if c1r == "whileloop":
            whileloop()

    if choice == "index":
        exindex()

    if choice == "inputs":
        inputs()

    if choice == "list":
        lists()

    if choice == "main":
        main()

    if choice == "numbers":
        num()

    if choice == "range":
        c1r = input(f'Choose: ex1range, ex2range: ')
        if c1r == "ex1range":
            ex1range()
        if c1r == "ex2range":
            ex2range()

    if choice == "variables":
        var()

if __name__ == '__main__':
    programs()

# "if __name___" function tells IDE that this script is for execution and not for importing into other files


