# 2. Loops (for, while)

print('something')
print('something')
print('something')
print('something')
print('something')

x = 0
y = 5

while x < y:
    print(x, 'something')
    x += 1

print('---------------------------------------1')

x = 0
y = 10

while x < y:
    print(x, 'something')
    x += 2

print('---------------------------------------2')

# nested while loops

a = 0
b = 0

while a < 5:
    a += 1
    print(a)
    while b < 5:
        b += 2
        print(b)

print('---------------------------------------3')

# ex1: 1 * 1 = 1

n = 1
m = 1

while n <= 9:
    while m <= 9:
        print(n, '*', m, '=', n*m)
        m += 1
    print()
    m = 1
    n += 1

print('---------------------------------------4')

# ex2:
num1 = 1
num2 = 1

while num1 <= 3:
    while num2 <= 3:
        print(num1, num2)
        num2 += 1
    num2 = 1
    num1 += 1

print('---------------------------------------4')

z1 = 1
z2 = 1
z3 = 1
times = 3

while z1 <= times:
    while z2 <= times:
        while z3 <= times:
            print(z1, z2, z3)
            z3 += 1
        z3 = 1
        z2 += 1
    z2 = 1
    z1 += 1













