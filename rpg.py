def skills():
    shield = int(input('What is your shield level? '))
    sword = int(input('What is your sword level? '))
    armor = int(input('What is your armor level? '))
    perception = int(input('What is your perception level?  '))

    if perception >= 30:
        print(f'You see that you need 40 shield, 45 sword, and 15 armor to continue')
    else:
        print('You do not know the required skill levels to progress, however...')

    if shield >= 40 and sword >= 45 and armor >= 15:
        print('You shall pass!')
    else:
        print('You shall not pass!')

def castle():
    print("You see a vampire castle ahead of you")
    age = int(input('How old are you? '))
    is_legally_dead = input('You are legally dead (True or False) ')
    VanH = input('You are Van Helsing (True or False) ')

    if age >= 50000 or is_legally_dead == "True" and not VanH == "True":
        print('You shall pass!')
    else:
        print('You shall not pass!')

# First condition is age. If age not met, checks to see if legally dead AND not Van Helsing
def opposite():
    print('Not True =', not True)
    print('Not False =', not False)