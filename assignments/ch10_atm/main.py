# Spencer Burton
# Chapter 10 ATM main

import Bank, Input

def main() :
    balance = Bank.ATM.get_balance()

    # Print starting balance
    print(str.format("Starting balance: ${:.2f}", balance))
    # Get amount to deposit from user
    amount = Input.Validator.get_float("Please enter deposit amount ($0.00 - $1000.00): ", 0.00, 1000.00)
    # Deposit amount
    balance = Bank.ATM.deposit(amount)
    # Print new balance
    print(str.format("New balance: ${:.2f}", balance))

    # Repeat everything before but for withdrawal
    amount = Input.Validator.get_float("Please enter withdrawal amount ($0.00 - $1000.00): ", 0.00, 1000.00)
    balance = Bank.ATM.withdraw(amount)
    print(str.format("New balance: ${:.2f}", balance))

main()
