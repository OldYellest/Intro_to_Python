from bool import numcheck, yearcheck, primecheck
from captial import capital
from for_while import exfor, exwhile, exloop, whileloop
from in_op import exin
from index import exindex
from inputs import inputs
from length import length
from list import lists
from lower import lower
from numbers import num, addrange
from plus import plus, mult
from range import ex1range, ex2range
from rpg import skills, castle, opposite
from setex import ex1, ex2, ex3
from stringex import excount, saw, glue
from variables import var

# from and imports only 'activate' once given function in script that references it
# Otherwise, function causes error
def main():
    print('Hello, World!!!')
def programs():
    program = (f"""Choose from the following programs:\n ~ bool, capital, for_while, in_op,\n ~ index, inputs, list, lower, length,\n ~ main, numbers, plus, range, rpg,\n ~ setex, stringex, variables""")
    print(program)
    choice = input(f'Select a program from the list above: ')


    if choice == "bool":
        c1r = input(f'Choose: numcheck, yearcheck, primecheck: ')
        if c1r == "numcheck":
            numcheck()
        elif c1r == "yearcheck":
            yearcheck()
        elif c1r == "primecheck":
            primecheck()
        else:
            return

    elif choice == "capital":
        capital()

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

    elif choice == "in_op":
        exin()

    elif choice == "index":
        exindex()

    elif choice == "inputs":
        inputs()

    elif choice == "length":
        length()

    elif choice == "list":
        lists()

    elif choice == "lower":
        lower()

    elif choice == "main":
        main()

    elif choice == "numbers":
        c1r = input(f'Choose: num, addrange: ')
        if c1r == "num":
            num()
        if c1r == "addrange":
            addrange()

    elif choice == "plus":
        c1r = input(f'Choose: plus, mult: ')
        if c1r == "plus":
            plus()
        if c1r == "mult":
            mult()

    elif choice == "range":
        c1r = input(f'Choose: ex1range, ex2range: ')
        if c1r == "ex1range":
            ex1range()
        if c1r == "ex2range":
            ex2range()

    elif choice == "rpg":
        c1r = input(f'Choose: skills, castle, opposite: ')
        if c1r == "skills":
            skills()
        if c1r == "castle":
            castle()
        if c1r == "opposite":
            opposite()

    elif choice == "setex":
        c1r = input(f'Choose: ex1, ex2, ex3: ')
        if c1r == "ex1":
            ex1()
        elif c1r == "ex2":
            ex2()
        elif c1r == "ex3":
            ex3()

    elif choice == "stringex":
        c1r = input(f'Choose: excount, saw, glue: ')
        if c1r == "excount":
            excount()
        if c1r == "saw":
            saw()
        if c1r == "glue":
            glue()

    elif choice == "variables":
        var()

if __name__ == '__main__':
    programs()

# "if __name___" function tells IDE that this script is for execution and not for importing into other files

