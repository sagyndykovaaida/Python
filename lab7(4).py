n = int(input())  
vacations = {}  

for i in range(n):
    last_name, day, month = input().split()
    if month in vacations:
        vacations[month].append(last_name)
    else:
        vacations[month] = [last_name]

query_month = input().strip()  

if query_month in vacations:
    print(" ".join(vacations[query_month]))
else:
    print() 
