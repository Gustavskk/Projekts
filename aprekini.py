import csv


with open("data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  
    data = [row for row in reader]


months = [row[0] for row in data]

total_expenses = []
remaining_income = []

for row in data:
    try:
        income = float(row[1].replace('$', ''))
        rent = float(row[2].replace('$', ''))
        food = float(row[3].replace('$', ''))
        electricity = float(row[4].replace('$', ''))
        subscriptions = float(row[5].replace('$', ''))
        transportation = float(row[6].replace('$', ''))

        total_expense = rent + food + electricity + subscriptions + transportation
        remaining = income - total_expense

        total_expenses.append(total_expense)
        remaining_income.append(remaining)
    except ValueError as e:
        print(f"Kļūda: {e}, rinda: {row}")


total_yearly_expenses = sum(total_expenses)
remaining_yearly_income = sum(remaining_income)


print("Mēnesis | Izterētie līdzekļi | Pāri palikušie līdzekļi")
print("-" * 50)
for month, exp, rem in zip(months, total_expenses, remaining_income):
    print(f"{month.ljust(9)}| {str(exp).ljust(18)}| {rem}")

print("\nKopējie gadā iztērētie līdzekļi:", total_yearly_expenses)
print("Pāri palikušie līdzekļi gadā:", remaining_yearly_income)
