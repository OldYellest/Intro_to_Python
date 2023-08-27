def num():
    x = 3
    y = 4
    num_1 = 14
    num_2 = 11
    num_3 = -9.9
    float_variable = 1.25
    integer_variable = 55

    print(f'Sum of num_1 and num_2 is: {num_1 + num_2}')
    print(f'Difference of num_1 and num_2 is: {num_1 - num_2}')
    print(f'Difference of num_2 and num_1 is: {num_2 - num_1}')
    print(f'Product of num_2 and num_1 is: {num_2 * num_1}')
    print(f'Quotient of num_2 and num_1 is: {num_2 / num_1}')
    print(f'Floored quotient of num_2 and num_1 is: {num_2 // num_1}')
    print(f'Remainder of num_1 / num_2 is: {num_1 % num_2}')
    print(f'Division and modulus of {num_1} and {num_2} is: {divmod(num_1, num_2)}')

# Floored quotient is division but answer is rounded down to closest integer
# Modulo or Modulus operation refers to the % sign
# Divmod returns div first, remainder second

    print(f'{float_variable} converted to an integer is: {int(float_variable)}')
    print(f'{integer_variable} converted to an float is: {float(integer_variable)}')
    print(f'The sum of {float_variable} and {integer_variable} is: {float_variable + integer_variable}')
    print(f'The sum of {float_variable} and {integer_variable} '
          f'converted to integer is: {int(float_variable + integer_variable)}')

# Any math involving a float operand will always produce a float result,
# unless converted to integer explicitly

    print(f'The absolute value of {num_3} is: {abs(num_3)}')

#abs gets you absolute value of number

    print(f'{3} to the power of {4} is: {pow(3, 4)}')
    print(f'{3} to the power of {4} is: {3 ** 4}')

# Both methods produce "power of" math
