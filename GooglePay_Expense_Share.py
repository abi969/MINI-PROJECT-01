users = []
balances = {}


def add_user():
    name = input("Enter user name: ")
    if name not in users:
        users.append(name)
        balances[name] = 0
        print(name, "added successfully!\n")
    else:
        print("User already exists!\n")

def add_expense():
    payer = input("Who paid the expense? ")
    
    if payer not in users:
        print("User not found!\n")
        return
    
    amount = float(input("Enter total amount: "))
    
    print("Users:", users)
    split_users = input("Enter users involved (comma separated): ").split(",")

    split_users = [user.strip() for user in split_users]

    share = amount / len(split_users)

    for user in split_users:
        if user != payer:
            balances[user] -= share
            balances[payer] += share

    print("Expense added successfully!\n")


def show_balances():
    print("\n--- Balances ---")
    for user in balances:
        if balances[user] > 0:
            print(user, "should receive ₹", round(balances[user], 2))
        elif balances[user] < 0:
            print(user, "should pay ₹", round(-balances[user], 2))
        else:
            print(user, "is settled up")
    print()

while True:
    print("1. Add User")
    print("2. Add Expense")
    print("3. Show Balances")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_balances()
    elif choice == "4":
        print("Thank you for using Expense Sharing App!")
        break
    else:
        print("Invalid choice!\n")
