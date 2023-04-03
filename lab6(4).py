names_str = input("Student ")
names_tuple = tuple(names_str.split())
for name in names_tuple:
    if "va"  in name:
        print(name, end=" ")