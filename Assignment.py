"""This assignment operators"""

# Assignment operator: =
the_price_of_cocaine = 100
print(the_price_of_cocaine)
vat = 0.19

# Assignment operator: +=
the_price_of_cocaine += 10
print(the_price_of_cocaine)

# Assignment operator: -=
the_price_of_cocaine -= 20
print(the_price_of_cocaine)

# Assignment operator: *=
the_price_of_cocaine *= 2
print(the_price_of_cocaine)

# Assignment operator: /=
the_price_of_cocaine /= 5
print(the_price_of_cocaine)
print(int(the_price_of_cocaine))

# Applying vat
the_price_of_cocaine += the_price_of_cocaine * vat
print(the_price_of_cocaine)
print("%.1f" % the_price_of_cocaine)

