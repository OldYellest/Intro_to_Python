def exfor():
    random_numbers = [4, 34, 5, 12, 64, 2, 4, 4, 55, 10, 0]
    multiples = []

    for hum in random_numbers:
        multiples.append(hum * 2)

    print(multiples)

# hum stands in as a definable string becomes a variable when used with 'in'
# To put function of numbers into a new list, must declare an empty list
# append() will impose the function in it's brackets into the multiples function
# The print function is outside the loop body to execute the function once

    print(dir(random_numbers))

# dir lists the types of functions supported in the for loop

def exwhile():
    number = 1
    while number < 11:
        print(number)
        number += 1

# while loops until condition is satisfied
def exloop():
    for x in range(1, 8):
        print()
        for y in range(1, 10):
            print(f'{x} x {y} = {x * y}')

# x prints the table with each y in the y range as
# x continues down the x range. Remember range is one less than last digit

def whileloop():
    m = 1
    for g in range(1, 3):
        print()
        while m < 10:
            print(f'{m} + {g} = {m + g}')
            m += 1
        for m in range(10):
            m += 1

# Needs work, will come back to later
