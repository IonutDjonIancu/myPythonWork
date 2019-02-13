"""
Substrings and string slicing
The belonging operator: in
"""

# belonging operator: in
sentence = "This is a sentence"

print("a" in sentence)  # outputs True
print("z" in sentence)  # outputs False

print("a" not in sentence)  # outputs False
print("z" not in sentence)  # outputs True

if "a" in sentence:
    print("'{}' contains a".format(sentence))

print(sentence[::-1])

# string slicing
a = "ABCD"

# [start position : end position : steps]
print(a[:1])
print(a[0:1])
print(a[0:1:1])
print(a[::2])
print()
print(a[3:1:-1])
print(a[0:4:2])

# replace
print("Z Z Z Z")
print("Z Z Z Z".replace("Z", "Y", 2))





















