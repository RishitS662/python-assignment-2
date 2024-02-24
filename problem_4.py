'''
Write a program that accepts a sequence of comma-separated numbers from the console and generates a list and a tuple that contains every number.

Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')
'''

numbers = input("Enter comma-separated numbers: ")
number_list = numbers.split(",")
number_tuple = tuple(number_list)

print(number_list)
print(number_tuple)
