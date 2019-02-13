"""
String manipulation
"""
text = "Aaaa"

print(text)
print(text.capitalize())
print(text[3:4].capitalize())
print(text.lower())
print(text.upper())

txt = text[3:4]

print(text, "\b\b", "\b" + txt.upper())

print(text.count("a"))

print("    SS SS".lstrip())
print("SS SS    ".rstrip())
print("    SS SS    ".strip())

print(text.swapcase())




