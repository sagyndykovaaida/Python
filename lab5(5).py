import random
all_numbers = list(range(1, 50))

ticket_num = random.sample(all_numbers, 6)
ticket_num.sort()
print("Lottery ticket numbers:")
for number in ticket_num:
    print(number)
