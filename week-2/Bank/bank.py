import random
import string
from account import SavingsAccount,CheckingAccount
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, password, *args):
        account_number = self.get_unique_acc_no()

        if account_type == 'savings':
            interest_rate, ifsc_code, joint_account = args
            account = SavingsAccount(account_number, password, interest_rate, ifsc_code, joint_account)
        elif account_type == 'checking':
            min_balance, ifsc_code = args
            account = CheckingAccount(account_number, password, min_balance, ifsc_code)

        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        return None

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts.values())
    
    def get_unique_acc_no(self)->int:
        while True:
            account_number = ''.join(random.choices(string.digits, k=10))
            if account_number not in self.accounts:
                return account_number
