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



