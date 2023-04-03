expenses = []
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    daily_expenses = {}
    print("Enter expenses for", day)
    daily_expenses["Transportation"] = float(input("Transportation: "))
    daily_expenses["Food"] = float(input("Food: "))
    daily_expenses["Entertainment"] = float(input("Entertainment: "))
    expenses.append(daily_expenses)
total_expenses = 0
for daily_expenses in expenses:
    for category, expense in daily_expenses.items():
        total_expenses += expense
print("Total expenses for the week:", total_expenses," KZT")