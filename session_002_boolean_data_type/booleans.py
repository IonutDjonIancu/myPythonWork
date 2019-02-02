# True
# False

x = 1
y = 2

"""Comparisons"""
# Equal operator: ==
print(x == y)

# Not equal operator: != (aka different or logical not)
print(x != y)

# Less than operator: <
print(x < y)

# Less than operator: >
print(x > y)

# Less than or equals to operator: <=
print(x <= y)

# Greater than or equals to operator: >=
print(x >= y)

"""Identity"""

x = 1
y = '1'

# Identity operator: is
print(x is y)

# Identity operator: is not
print(x is not y)

"""Boolean logic"""
# AND via Anding
print(True and True)
print(True and False)
print(False and False)
# OR
print(True or True)
print(True or False)
print(False or False)

"""Boolean logic examples"""
print(1 < 2 and 2 <= 2)
print(1 < 2 and 2 < 2)

print(1 < 2 or 2 < 2)
print(1 < 2 or 2 < 2)

print(1 < 2 or 2 <= 2 or 1 < 2 or 2 <= 2)

"""Combined AND with OR"""
print(True and True or False)
print((True and True) or False)

"""Optional"""
x = 0
y = 2

print()
print(x and y)

"""Storing booleans in memory"""
bool1 = True
print(bool1)

bool1 = 1 < 2
print(bool1)

bool1 = 1 == 2
print(bool1)

bool1 = 1 < 2 or 4 < 6
print(bool1)

"""Negation operator"""
bool1 = not(1 < 2 or 4 < 6)
print(bool1)




















