# commenters = set()  

# while True:
#     line = input().strip()
#     if not line: 
#         break
#     name = line.split(':')[0].strip() 
#     commenters.add(name)  

# print(len(commenters))  


comments = {}
unique_commenters = []

while True:
    entry = input("Name and comment ")
    if entry == "":
        break
    name, comment = entry.split(": ")
    if name not in comments:
        comments[name] = [comment]
    else:
        comments[name].append(comment)

for name in comments:
    unique_commenters.append(name) 

print("Total number commenters:", len(unique_commenters))
