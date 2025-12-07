print('Phase-1 Started coding')

# Adding two numbers

number1 = int(input('Enter the 1st Number: '))
number2 = int(input('Enter the 2nd Number: '))
print(number1+number2)


# Finding the given number postive or negative
number_check = int(input('Enter the number for Testing: '))
if number_check > 0:
    print('The number is postive(+)')
elif number_check < 0:
    print('The number is negative(-)')
else:
    print('The number is zero(0)')



# Check the number is even or odd

check_even_odd = int(input('Enter the Number to check Even or Odd'))
if check_even_odd%2 == 0:
    print(f'The Number is even: {check_even_odd}')
else:
    print(f'The Number is Odd: {check_even_odd}')


# check for the largest Number in 3 Numbers

input1 = int(input('Enter the first Number: '))
input2 = int(input('Enter the second Number: '))
input3 = int(input('Enter the third Number: '))

if input1 == input2 == input3:
    print('All the numbers are equal')
biggest = input1
if input2 > biggest:
    biggest = input2
if input3 > biggest:
    biggest = input3
print(f'The biggest Number is {biggest}')

# Formate the sentence 

name = input('Enter Your Name: ')
age = int(input('Enter the AGE: '))
print(f'The name of the person is {name}. The age of the person {age}')


# Converng KM into Miles

distance = int(input('Enter the KM to convert into miles'))

print(f'The total {distance}km in miles is {(0.62 * distance):.2f}')


# Converting the C to F (32°F − 32) × 5/9

Celsius = int(input('Enter the Celsius to convert: '))
print(f'Fahrenheit: {Celsius * 1.8 + 32}')


# Enter the string to calculate the length

string1 = intput('Enter the string: ')
print(f'Total length of string: {len(string1.rstrip())}')


# Reverse the string
str1 = input('Enter the 1st String to reverse: ')
str2 = input('Enter the 2nd String to reverse: ')
print(f' The revere of the string is {str1[::-1]}')
print(f' The revere of the string is {str2[::-1]}')


# Simple calculator

input1 = int(input('Enter the number1 '))
input2 = int(input('Enter the number2 '))
operation = input('Enter the operator to perform: (+ - * / % //)')

if operation == '+':
    result = input1 + input2
elif operation == '-':
    result = input1 - input2
elif operation == '*':
    result = input1 * input2
elif operation == '/':
    result = input1 / input2
elif operation == '%':
    result = input1 % input2
elif operation == '//':
    result = input1 // input2
else:
    result = "Invalid operator!"

print(f'The result of operation is: {result}')
