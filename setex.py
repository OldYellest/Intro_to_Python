def ex1():
    numbers = {1, 2, 3, 4, 5}

    for X in numbers:
        print(X)

# This will list all the numbers in the set on a 1 input per line output
# 1
# 2
# 3, etc.
# A new set can be created between curly brackets, but cannot create empty set, which needs set function

def ex2():
    numbers = {}

    print('Numbers = {}')
    print(type(numbers))

    numbers = set()

    print('Numbers = set()')
    print(type(numbers))

# Empty curly brackets creates a dictionary
# Set function creates an empty set
# Sets are similar to lists, but cannot put duplicate values in set

def ex3():
    numlist = [1, 2, 3, 4, 5, 5, 3, 1, 2]

    print(f'Numbers List: {numlist}')

    numset = set(numlist)
    print(f'Numbers Set: {numset}')

    print('We now add 199 to the set')
    numset.add(199)
    print(f'New Added Numbers Set: {numset}')

    print('We now take away 4 from the set')
    numset.discard(4)
    print(f'New Discarded Numbers Set: {numset}')

    print('We now clear the set')
    numset.clear()
    print(f'New Cleared Numbers Set: {numset}')
# Sets are mutable, new values can be added and discarded
