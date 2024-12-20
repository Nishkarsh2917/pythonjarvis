import csv
import json

class Expense:
    def __init__(self, date, category, amount, description=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

def load_expenses(filename, filetype='csv'):
    if filetype == 'csv':
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            return [Expense(*row) for row in reader]
    elif filetype == 'json':
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Expense(d['date'], d['category'], d['amount'], d.get('description', '')) for d in data]

def save_expenses(expenses, filename, filetype='csv'):
    if filetype == 'csv':
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            for expense in expenses:
                writer.writerow([expense.date, expense.category, expense.amount, expense.description])
    elif filetype == 'json':
        with open(filename, 'w') as file:
            json.dump([vars(expense) for expense in expenses], file, indent=4)

def calc_total_spending(expenses):
    total = 0.0
    for expense in expenses:
        total += expense.amount
    return total

def calc_spending_by_category(expenses):
    categories = {}
    for expense in expenses:
        categories[expense.category] = categories.get(expense.category, 0.0) + expense.amount
    return categories

def plot_spending_by_category(categories):
    import matplotlib.pyplot as plt
    import seaborn as sns 
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(categories.keys()), y=list(categories.values()))
    plt.xlabel('Category')
    plt.ylabel('Total Spending')
    plt.title('Spending by Category')
    plt.xticks(rotation=45)
    plt.show()

expenses = load_expenses('expenses.csv') 

total_spending = calc_total_spending(expenses)
print(f"Total Spending: ${total_spending:.2f}")

spending_by_category = calc_spending_by_category(expenses)
print("\nSpending by Category:")
for category, amount in spending_by_category.items():
    print(f"{category}: ${amount:.2f}")

plot_spending_by_category(spending_by_category)

save_expenses(expenses, 'expenses.json')
