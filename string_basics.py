#how to make a multiline string
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

#how to make quatation marks part of the string
my_str_5 = 'I\'m learning Python'
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
#or
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'


#how to concatenate strings
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

#or using f-strings

name = 'Khalidah Aminah'
age = 17
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is Khalidah Aminah and I am 17 years old

#f-strings can also be used to perform calculations
num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

#small exercise
first_name = 'khalidah'
last_name = 'aminah'
full_name = f'My name is {first_name} {last_name}, nice to meet you!'
print(full_name) # My name is khalidah aminah, nice to meet you!