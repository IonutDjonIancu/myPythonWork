"""Control flow (aka Decision Making)"""
# 1. Conditional Statements (if, elif, else)
# 2. Loops (for, while)

min_driving_age = 16
max_driving_age = 90
min_voting_age = 18
min_drinking_age = 21

my_age = 15

if my_age <= min_driving_age:
    print('you are too young to drive')

if min_driving_age <= my_age < max_driving_age:
    print('you can drive')

# ternary operator
print('you can vote') if my_age >= min_voting_age else print('no vote')

if my_age >= min_driving_age:
    print('you can drink')
else:
    print('you cannot drink')

print('=====================================1')

my_age = 25

if my_age >= min_driving_age:
    print('you can drive')
if my_age >= min_voting_age:
    print('you can vote')
if my_age >= min_drinking_age:
    print('you can drink')

print('=====================================2')

my_age = 91

# if min_driving_age <= my_age <= max_driving_age:
if min_driving_age <= my_age | max_driving_age <= my_age:
    print('you can drive')
    if my_age >= min_voting_age:
        print('you can vote')
        if my_age >= min_drinking_age:
            print('you can drink')


print('=====================================3')























