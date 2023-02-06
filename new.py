line, upp, low = input(), 0, 0
for symb in line:
    if symb.isalpha() and symb.isupper():
        upp += 1
    elif symb.isalpha() and symb.islower():
        low += 1
print(line.upper()) if upp > low else print(line.lower())
