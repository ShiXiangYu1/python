# Write your code here
# Write your code here
print('Earned amount:')
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
count=float(202 + 118 + 2250 + 1680 + 1075 + 80)
print()
print("Income: $"+ str(count))
staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
net_income = count - staff_expenses - other_expenses
print(f"Net income: ${net_income}")