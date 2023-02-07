a, b = input(), input()
while not(a.isdigit() and b.isdigit()):
    a, b = input(), input()
print(int(a) + int(b))
