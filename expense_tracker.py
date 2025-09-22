import json

FILENAME = "expenses.json"

def loadexpense():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def saveexpense(expense):
    with open(FILENAME, "w") as f:
        json.dump(expense, f, indent=4)
import json

FILENAME=expense.json

def loadExpenses():
try:
with open(FILENAME,"r") as f:
return json.load(f)
except FileNotFoundError:
return []

def saveExpenses():
with open(FILENAME, "w") as f:
json.dump(expenses, f, indent=4)

def addexpense(expense):
    item = input("Item: ")
    amount = float(input("Amount: "))
    expense.append({"item": item, "amount": amount})
    saveexpense(expense)
    print("Expense added!")

def showexpense(expense):
    print("\nYour Expense:")
    for e in expense:
        print(f"{e['item']} - ${e['amount']}")  
    total = sum(e['amount'] for e in expense)
    print(f"Total: ${total}\n")

def main():
    expense = loadexpense()
    while True:
        choice = input("Add expense (a)/ Show expense (s)/ Quit (q): ").lower()
        if choice == "a":
            addexpense(expense)
        elif choice == "s":
            showexpense(expense)
        elif choice == "q":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()


