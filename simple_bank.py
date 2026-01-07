

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():

    try:
        amount = float(input("Enter an amount to be deposited: \t"))
    except ValueError:
        print("Please enter amount in a integer: \t")
    if amount < 0:
        print("Invalid Amount")
        return 0
    
    return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: \t"))

    if amount < 0:
        print("Invalid Amount")
        return 0
    elif amount > balance:
        print("Insufficient balance.")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit Balance ")
        print("3. Withdraw Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): \t")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif  choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Input is invalid.")
    print("Thank You, Have a nice day.")

if __name__ == "__main__":
    main()