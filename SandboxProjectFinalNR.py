import os

class BankAccount:
    def __init__(self, username, account_type, balance=0):

        self.username = username
        self.account_type = account_type.lower()  
        self.balance = balance
        self.account_number = id(self)  
        self.filename = f"{self.account_number}_{self.account_type}_{self.username}.txt"

        
        with open(self.filename, 'w') as file:
            file.write(f"Account ID: {self.account_number}\n")
            file.write(f"Account Holder: {self.username}\n")
            file.write(f"Account Type: {self.account_type.capitalize()}\n")
            file.write(f"Initial Balance: ${self.balance:.2f}\n")
            file.write("Transaction History:\n")

   
    def deposit(self, amount):

        self.balance += amount
        with open(self.filename, 'a') as file:
            file.write(f"Deposited: ${amount:.2f} | New Balance: ${self.balance:.2f}\n")

   
    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            return False
        self.balance -= amount
        with open(self.filename, 'a') as file:
            file.write(f"Withdrew: ${amount:.2f} | New Balance: ${self.balance:.2f}\n")
        return True

    
    def get_balance(self):

        return self.balance

    
    def get_user_id(self):

        return self.account_number

    def get_username(self):

        return self.username

    def get_account_type(self):

        return self.account_type

    
    def get_transaction_history(self):

        with open(self.filename, 'r') as file:
            return file.read()


if __name__ == "__main__":
    
    account1 = BankAccount("Nathi", "Chequing", 1000)
    account2 = BankAccount("Taylor", "Savings", 500)

    
    account1.deposit(200)
    account2.deposit(300)

    
    account1.withdraw(50)
    account2.withdraw(700)  

    
    print("Account 1 Balance:", account1.get_balance())
    print("Account 2 Balance:", account2.get_balance())

    
    print("\nAccount 1 Transaction History:")
    print(account1.get_transaction_history())

    print("\nAccount 2 Transaction History:")
    print(account2.get_transaction_history())

