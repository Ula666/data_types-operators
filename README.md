# Introduction to Python Data types and Operators

- Strings
- numbers Integers, floats, longs
- Boolean (True or False)

### Arithmetic Operators
### Comparison Operators

- Arithmetic Operators
```python
+, -, *, /
```
- Modulus
``` %``` It gives the remainder of the 2 numbers
- Comparison Operators
  ``` >, <, >=, <=, ==, !=```
  

# #indexing in Python starts from 0
- `H e l l o   w o r l d !`
- `0 1 2 3 4 5 6 7 8 9 10 11`
- `-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1`

### Lets  have a look at some string methods
white_space = "lot's of space at the end         "
### strip() function helps us delete all white spaces
- print(len(white_space))
- print(len(white_space.strip())) # doesnt show empty spaces

### counts the number of times the word is mentioned in a text
- ```Example_text = "here's Some texts with lot's of text"```
- ```print(Example_text.count("text"))```
- ```print(Example_text.upper())```
- ```print(Example_text.lower())```
- ```print(Example_text.capitalize())``` 
### capitalized the first letter of the string
- ```print(Example_text.replace("with", ","))``` 
### replaces word with a new specified one


### Concatenation and Casting

```print(first_name + " " + last_name)```

```print(first_name + " " + last_name + " " + str(age))```
- we have to change int to string/cast string into int

### F - string is and amazing magical formatting f
```print(f"{first_name} {last_name} is {age} old")```