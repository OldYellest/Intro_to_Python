def inputs():
    # name = input('What is your name? ')
    # age = int(input(f'How old are you {name}? '))
    # year = int(input('What year is this? '))

    # print(f'Well, it is nice to meet you {name}. '
    #     f'If I am right, you were born in the year of our Lord {year - age}.')

    tempC = input(' What is the temperature in celsius? ')
    tempF = (float(tempC) * 1.8) + 32
    print(f'{tempC} degrees celsius is {tempF} degrees fahrenheit.')