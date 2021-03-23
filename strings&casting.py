# Strings and Casting

# Let's have a look at some industry practices
# single and double quotes examples

# single_quotes = 'single quotes  \'WoW\''
# double_quotes = "double quotes 'WOW'"
# print(single_quotes)
# print(double_quotes)

# String slicing

greetings = "hello world!" # string
# indexing in Python starts from 0
# H e l l o   w o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11
#  -10                      -3 -2 -1
# how can we find out the length of this statement
#
# we have a method called len() to find out the length of the statement

# print(greetings[0:5]) # outputs Hello starting from 0 to 4, not including 5
# print (greetings[6:11])

# reverse indexing starts with -1
# print (greetings[-1]) # output the last character
# print (greetings[:-6]) # it will output the word hello

# Lets  have a look at some string methods
# white_space = "lot's of space at the end         "
# # strip() function helps us delete all white spaces
# print(len(white_space))
# print(len(white_space.strip())) # doesnt show empty spaces

# counts the number of times the word is mentioned in a text
# Example_text = "here's Some texts with lot's of text"
# print(Example_text.count("text"))
# print(Example_text)
# print(Example_text.upper())
# print(Example_text.lower())
# print(Example_text.capitalize()) # capitalized the first letter of the string
# print(Example_text.replace("with", ",")) # replaces word with a new specified one

# Concatenation and Casting
first_name = "Ula"
last_name = "Walker"
age = 99 #int
# print(first_name + " " + last_name)
# print(first_name + " " + last_name + " " + str(age)) # we have to change int to string, to cast string into int
# print(type(int(age)))

# F - string is and amazing magical formatting f
print(f"Your First name is {first_name} and your last name is {last_name} and you are {age} years old.")


















