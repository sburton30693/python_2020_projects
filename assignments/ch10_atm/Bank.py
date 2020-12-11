# Spencer Burton
# ATM class

class ATM :
    balance = 20.00

    def deposit(amount) :
        # Print amount being deposited
        print(str.format("Depositing ${:.2f}", amount))
        ATM.balance += amount

        return ATM.balance

    def withdraw(amount) :
        if ATM.balance >= amount :
           print(str.format("Withdawing ${:.2f}", amount))
           ATM.balance -= amount
        else :
            print("Insufficient funds")

        return ATM.balance

    def get_balance() :
        return ATM.balance
