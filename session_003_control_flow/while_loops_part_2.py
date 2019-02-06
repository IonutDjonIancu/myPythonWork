"""
1. while + if
2. while + if + and/or
3. break / continue

"""


a = True
b = True
while a:
    a = b
    print(a)
    if a:
        break
    a = False

print('--------------------------1')

a = 1
b = 2

while a <= 3 and b <= 3:
    if a == 2 or b == 2:
        print('two')
    else:
        print(a)
    a += 1
    b += 1

print('--------------------------2')

x = 1
while x <= 3:
    if x == 2:
        x += 1
        continue
    print(x)
    x += 1

print('--------------------------2')

a, b, c, d = 1, 1, 1, 1  # same as: a = b = c = d = e = 1

limit = 10

while a <= limit:
    while b <= limit:
        while c <= limit:
            while d <= limit:
                print(a, b, c, d)
                d += 1
            c += 1
            d = 1
        b += 1
        c = 1
    a += 1
    b = 1

print('--------------------------2')
















