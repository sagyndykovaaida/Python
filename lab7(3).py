n = int(input())  
phone_book = {}  

for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone

query = input().strip() 

if query in phone_book:
    print(phone_book[query])
else:
    print("Not in the phone book.")
