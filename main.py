from inputs import inputs
from list import lists
from numbers import num
from variables import var

#from and imports only 'activate' once given function in script that refrences it
#Otherwise, function causes error

def main():
    print('Hello, World!!!')

def programs():
    program = ("inputs", 'list', 'main', 'numbers', 'variables')
    print(program)
    choice = input(f'Select a program from the list above: ')

    if choice == "inputs":
        inputs()

    if choice == "list":
        lists()

    if choice == "main":
        main()

    if choice == "numbers":
        num()

    if choice == "variables":
        var()

if __name__ == '__main__':
    programs()

# "if __name___" function tells IDE that this script is for execution and not for importing into other files


