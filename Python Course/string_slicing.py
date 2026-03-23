# We can access each character in a string by using its index number. 
# The first character has an index of 0, the second character has an index of 1, and so on.
# We can also use negative indexing to access characters from the end of the string, where the last character has an index of -1, 
# the second to last character has an index of -2, and so on.

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

# We can use slicing to make a range of characters in a string. 
# The syntax for slicing is: string[start:end]
# where start is the index of the first character you want to include, and end is the index of the first character you want to exclude.

print(my_str[0:5])  # Hello
print(my_str[6:11]) # world
print(my_str[:5])   # Hello (start is 0 by default)
print(my_str[6:])   # world (end is the length of the string by default)
print(my_str[:])    # Hello world (start and end are the defaults, so it includes the whole string)

my_str = 'Hello world'
print(my_str[1:4]) # ell

#slicing doesnt change the original string
print(my_str) # Hello world

#theres also a step parameter, which can extract character at specific intervals. The syntax is: string[start:end:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd, which means it starts at index 0, goes up to index 11 (exclusive), and takes every 2nd character.

#this step parameter also allows u to reverse a string by using a -1 step
my_str = 'Hello world'
print(my_str[::-1])  # dlrow olleH, it goes backwards.