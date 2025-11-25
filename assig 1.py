#List to store data
categories = []
amounts = []

print("===== Simple Expense Tracker =====")

while True:
    category = input("Enter expense category (e.g. Food, Travel, Bills): ")
    amount = float(input("Enter amount spent: INR"))
    
    categories.append(category)
    amounts.append(amount)
    #Asking if user wants to add more 
    more = input("Add another expense? (yes/no): ").lower()
    if more != 'yes':
        break

total_expense = sum(amounts)
num_entries = len(amounts)
average_expense = total_expense / num_entries if num_entries > 0 else 0
#Output Results
print("\n===== Expense Summary =====")
for i in range(len(categories)):
    print(f"{i+1}. Category: {categories[i]:<15} Amount: INR{amounts[i]:.2f}")

print(f"\nTotal Expenses: INR{total_expense:.2f}")
print(f"Average Expense: INR{average_expense:.2f}")

#Save to text file
with open("expenses.txt", "w") as file:
    file.write("=============== Expense Summary ===============\n")
    for i in range(len(categories)):
        file.write(f"{i+1}. Category: {categories[i]:<15} Amount: INR{amounts[i]:.2f}\n")
    file.write(f"\nTotal Expenses: INR{total_expense:.2f}\n")
    file.write(f"Average Expense: INR{average_expense:.2f}\n")
    file.write(f"Average Expense per Entry: INR{average_expense:.2f}\n")

print("\nAll data saved to 'expenses.txt'")