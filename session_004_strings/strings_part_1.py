"""
Strings are literal data types
"""

x = 'this is a string'
print(x)
x = "this is a new string"
print(x)
print(repr(x))

print("A")
print(repr("A"))

print('she said i\'m "small"')

# Escape character \:

print('\'')
print('\'\'')
print("'")
print("''")

# Special characters:
print('==========')
print('\n')             # the new line character
print('==========')
print('====\t======')   # the tab character (indents for the default number of spaces)
print('\u221a')         # the UTF encoding
print('!!\b')           # backspacing and deleting last character
print('nⁿ')             # alt characters
print('°')              # alt-0176

# String conversions:
print(str(120))         # converts numeric values to string
print(repr(str(120)))
print(str(120.25))      # converts numeric values to string

# String concatenation:

print(1 + 1)            # + is the addition operator
# print(1 + '1')          # returns error
print(str(1) + '1')     # + becomes the concatenation operator

print('A' + 'B')
print('A', '\bB')

# Extra (convert strings to numbers)
print(int(1.5))
print(float(2))

print(int('44') + 1)































