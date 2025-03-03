import os
from datetime import datetime

# Implement the log_transaction decorator function
def log_transaction(func):
    def wrapper(self,*args, **kwargs):
        res = func(self,*args, **kwargs)
        if not os.path.exists("transactions"):
            os.makedirs("transactions")
        transaction_type = func.__name__
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account_number = self.account_number
        amount = args[0] if args else 0
        log_message = f"[{timestamp}]: Transaction Type: {transaction_type}, Account Number: {account_number}, Amount: {amount}\n"
        file_path = f"transactions/{account_number}.txt"
        with open(file_path, "a") as file:
            file.write(log_message)

        return res
    return wrapper

class Account:
    # Implement the Account class
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = 0.0

    @log_transaction
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    @log_transaction
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    # Implement the SavingsAccount class
    def __init__(self, account_number, password, interest_rate, ifsc_code, joint_account=False):
        super().__init__(account_number, password)
        self.interest_rate = interest_rate
        self.ifsc_code = ifsc_code
        self.joint_account = joint_account

    @log_transaction
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Applied interest. New balance: {self.balance}")


class CheckingAccount(Account):
    # Implement the CheckingAccount class
    def __init__(self, account_number, password, min_balance, ifsc_code):
        super().__init__(account_number, password)
        self.min_balance = min_balance
        self.ifsc_code = ifsc_code

    @log_transaction
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(
                f"Cannot withdraw.You need minimum balance of {self.min_balance}.")
