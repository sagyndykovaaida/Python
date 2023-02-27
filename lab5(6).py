def is_sorted(lst):
   
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

num = input("Enter a list of numbers: ").split()
num = [int(number) for number in num]

if is_sorted(num):
    print("The list is sorted!")
else:
    print("The list is not sorted.")
