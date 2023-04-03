
n = int(input())
dictionary = {}

for i in range(n):
    line = input().split()
    country = line[0]
    rivers = line[1:]
    for river in rivers:
        dictionary[river] = country


river_names = input().split()

for river in river_names:
    if river in dictionary:
        print(river, "flows through", dictionary[river])
    else:
        print("The country for", river, "is not in the dictionary")

new_river = input("Enter the name of a river: ")
if new_river in dictionary:
    print(new_river, "is in the dictionary")
else:
    print(new_river, "is not in the dictionary")
 
new_country = input("country name: ")
new_river = input("river name: ")
dictionary[new_river] = new_country
print("The new pair", new_country, "-", new_river, "has been added to the dictionary")
