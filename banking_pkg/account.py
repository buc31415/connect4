"""
This module is called by app.py. It requires the float variable <balance> to 
check balance, add or withdraw money. This module also has code to exit the program.
"""

# checks account balance


def show_balance(balance):
    print(f"Current balance:  ${balance:,.2f}")

# makes a deposit


def deposit(balance):
    dep_amount = float(input("Enter amount to deposit:  "))
    balance = balance + dep_amount
    print(f"Current balance:  ${balance:,.2f}")
    return balance

# withdraws funds


def withdraw(balance):
    withdraw_amount = float(input("Enter amount to withdraw:  "))
    if withdraw_amount > balance:  # insuffienct funds
        print("Where are you going to get that amount of money?")
    else:
        balance = balance - withdraw_amount
    print(f"Current balance:  ${balance:,.2f}")
    return balance

# exits the interface


def logout(name):
    print(f"Goodbye {name}")
