def numcheck():
    number = int(input('what number would you like to check?\n- '))

    # \n uses the next line to print

    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

# == checks if value on left is equal to value on right

def yearcheck():
    year = int(input('Which year would you like to check?\n- '))

    if year % 400 == 0 and year % 100 == 0:
        print(f'{year} is a leap year')
    elif year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year.')

# elif takes over if "if" fails, instead of checking for both at same time
# "and" requires both sides to be true to return as true

def primecheck():
    number = int(input('What number would you like to check as a prime?\n- '))

    # is_not_prime = False

   # if number == 1:
    #    print(f'{number} is not a prime number')
    # elif number > 1:
     #   for n in range(2, number):
      #      if (number % n) == 0:
       #         is_not_prime = True
        #        break

       # if is_not_prime:
        #    print(f'{number} is not a prime number')
        # else:
         #   print(f'{number} is a prime number')

# 1 is not a prime number, but is a special case, so it is written that 1 is out as it's own
# number is then checked for > 1, then checked for divisibility for all numbers between 2 and the number
# loop closes when all numbers are checked or break if number is divisable by number before it
# pre-exisiting condition is changed when new condition is met
# break will end the loop, while 'continue' can skip current iteration instead of breaking out

    if number == 1:
        print(f'{number} is not a prime number')
    elif number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                print(f'{number} is not a prime number')
                break
        else:
            print(f'{number} is a prime number')

# Method is done without pre-existing condition (is_not_prime)
# else statement is executed one for loop is completed, break will close whole elif statement

