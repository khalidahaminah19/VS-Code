# Common methods for string manipulation

#upper() - Converts a string to uppercase
my_str = 'hello world'
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

#lower() - Converts a string to lowercase
my_str = 'hELlO WoRLD'
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

#strip() - Removes leading and trailing whitespace from a string
my_str = '  hello world  '
stripped_my_str = my_str.strip()
print(stripped_my_str)  # hello world

#replace(old, new) - Replaces a specified substring with another substring
my_str = 'hello world'
replaced_my_str = my_str.replace('world', 'Ami')
print(replaced_my_str)  # hello Ami

#split(separator) - Splits a string into a list of substrings based on a specified delimiter
my_str = 'hello,world'
split_my_str = my_str.split(',')
print(split_my_str)  # ['hello', 'world']

#join(iterable) - Joins a list of strings into a single string, using a specified separator
my_list = ['hello', 'world']
joined_str = ','.join(my_list)
print(joined_str)  # hello,world

#startswith(prefix) - Checks if a string starts with a specified prefix and returns True or False
my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

#endswith(suffix) - Checks if a string ends with a specified suffix and returns True or False
my_str = 'hello world'
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

#find(substring) - Returns the index of the first occurrence of a specified substring, or -1 if the substring is not found
my_str = 'hello world'
find_my_str = my_str.find('world')
print(find_my_str)  # 6

#count(substring) - Returns the number of occurrences of a specified substring in a string
my_str = 'hello world'
count_my_str = my_str.count('l')
print(count_my_str)  # 3

#capitalize() - Capitalizes the first letter of a string
my_str = 'hello world'
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

#isupper() - Checks if all characters in a string are uppercase and returns True or False
my_str = 'HELLO WORLD'
is_upper = my_str.isupper()
print(is_upper)  # True

#islower() - Checks if all characters in a string are lowercase and returns True or False
my_str = 'hello world'
is_lower = my_str.islower()
print(is_lower)  # True

#title() - Converts the first character of each word in a string to uppercase and the rest to lowercase
my_str = 'hello world'
title_my_str = my_str.title()
print(title_my_str)  # Hello World










# ==================== EXERCISE ====================
# String Common Methods Exercise

# Exercise 1: String Processing
# Given: user_input = '   Python Programming   '
# Task: Remove leading/trailing whitespace and convert to uppercase
user_input = '   Python Programming   '
# TODO: Write code here to clean and uppercase the string
output_clean_upper = user_input.strip().upper()
print(output_clean_upper)

# Exercise 2: Email Validation
# Given: email = 'User@Example.COM'
# Task: Convert to lowercase and check if it ends with '.com'
email = 'User@Example.COM'
# TODO: Convert email to lowercase and check if it ends with '.com'
email_lwr = email.lower()
print(email_lwr)
email_suffix = email_lwr.endswith('.com')
print(email_suffix)

# Exercise 3: Text Replacement
# Given: sentence = 'I love Python. Python is great. Python is fun!'
# Task: Replace 'Python' with 'JavaScript' and count how many replacements were made
sentence = 'I love Python. Python is great. Python is fun!'
# TODO: Replace Python with JavaScript and count occurrences of 'Python' before replacement
change_java = sentence.replace('Python', 'JavaScript')
print(change_java)
count_python = sentence.count('Python')
print(count_python)


# Exercise 4: String Splitting and Joining
# Given: csv_data = 'apple,banana,orange,grape'
# Task: Split the string by comma, convert each fruit to title case, and join with hyphen
csv_data = 'apple,banana,orange,grape'
# TODO: Split, convert to title case, and join with hyphen
csv_split = [fruit.title() for fruit in csv_data.split(',')]
print(csv_split)
csv_join = '-'.join(csv_split)
print(csv_join)


# Exercise 5: Password Validation
# Given: password = 'MyPassword123'
# Task: Check if password starts with 'My', is not all uppercase, and is not all lowercase
password = 'MyPassword123'
# TODO: Check the three conditions above
checkpw = password.startswith('My')
print(checkpw)
uppercheck = not password.isupper()
print(uppercheck)
lowercheck = not password.islower()
print(lowercheck)


# Exercise 6: Find and Extract
# Given: text = 'The quick brown fox jumps over the lazy dog'
# Task: Find the position of 'fox' and count how many times the letter 'o' appears
text = 'The quick brown fox jumps over the lazy dog'
# TODO: Find position of 'fox' and count letter 'o'
find_text = text.find('fox')
print(find_text)
count_text = text.count('o')
print(count_text)


# Exercise 7: Text Formatting
# Given: title = 'data science and machine learning'
# Task: Convert to title case, then capitalize first letter (bonus: explain the difference)
title = 'data science and machine learning'
# TODO: Apply title() and capitalize() and compare results
app_title = title.title()
print(app_title)
app_cap = title.capitalize()
print(app_cap)
print('The difference is "title()" capitalizes every first letter from each word in the title. ' \
'Meanwhile, "capitalize()" only capitalizes the first letter of the entire string.')

# Exercise 8: String Cleaning
# Given: dirty_text = '  hello     WORLD   from   python  '
# Task: Strip whitespace, convert to lowercase, and split into words
dirty_text = '  hello     WORLD   from   python  '
# TODO: Clean and split the text
clean_text = dirty_text.strip()
print(clean_text)
lwr_text = clean_text.lower()
print(lwr_text)
split_text = lwr_text.split()
print(split_text)