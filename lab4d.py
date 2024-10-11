#!/usr/bin/env python3

# Author ID: Yahmad4

# Strings 1
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_str):
    """Returns the first five characters of the given string."""
    return input_str[:5]

def last_seven(input_str):
    """Returns the last seven characters of the given string."""
    return input_str[-7:]

def middle_number(input_num):
    """Returns the second and third characters of the given number."""
    num_str = str(input_num)  # Convert the number to a string
    return num_str[1:3]       # Return characters at index 1 and 2

def first_three_last_three(str1, str2):
    """Returns the first three characters of str1 and the last three characters of str2 combined."""
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))  # Output: 'Hello'
    print(first_five(str2))  # Output: 'Senec'
    print(last_seven(str1))  # Output: 'World!!'
    print(last_seven(str2))  # Output: 'College'
    print(middle_number(num1))  # Output: '50'
    print(middle_number(num2))  # Output: '.5'
    print(first_three_last_three(str1, str2))  # Output: 'Helege'
    print(first_three_last_three(str2, str1))  # Output: 'Send!!'
