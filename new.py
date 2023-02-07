str, upp, low = input(), 0, 0
for symb in str:
    if symb.isalpha() and symb.isupper():
        upp += 1
    elif symb.isalpha() and symb.islower():
        low += 1
print(str.upper()) if upp > low else print(str.lower())
