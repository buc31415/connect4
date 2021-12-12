""" 
This module mimics an ATM allowing a user to check balance, make deposits and make 
withdrawals. It builds a user interface to create and validate an account, and 
holds the account balance. Account update functions are maintained in accounts.py 
in banking_pkg.
 """

# Get functions to check balance, make a deposit or withdrawal, and log out
from banking_pkg import account

# menu interface


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# Create user w user name no more than 10 characters
print('=== Automated Teller Machine ===')
name = input("Enter name to register: ")
while len(name) > 10 or len(name) < 1:
    print("Your user name must be 10 characters long.")
    name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0.0
print(f"Enter name to register: {name}")
print(f"Enter PIN: {pin}")
print(f"{name} has been registered with a starting balance of ${balance:,.2f}.")

# Validate user with name and pin
user_validated = False
while not user_validated:
    print('=== Automated Teller Machine ===')
    name_to_validate = input("Enter name:  ")
    pin_to_validate = input("Enter PIN:  ")
    if pin == pin_to_validate and name == name_to_validate:
        print("Login successful!")
        user_validated = True
    else:
        print("Invalid credentials")

# What does the user want to do? [check balance, add/remove money, exit]
menu_option = False
while menu_option == False:
    atm_menu(name)  # call interface
    option = input("Choose an option:  ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid selection. Try again")
