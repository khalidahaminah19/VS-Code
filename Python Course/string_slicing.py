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