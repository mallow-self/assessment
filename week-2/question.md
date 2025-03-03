## Question 1:

**Python test question:**

- You are required to implement a banking program using Python.

- The program should allow users to create accounts, deposit and withdraw funds, view their balance, and log all transactions.

- You can use the following code skeleton as a starting point:

```Python
import os
import random
import string
from datetime import datetime

# Implement the log_transaction decorator function

class Account:
    # Implement the Account class

class SavingsAccount(Account):
    # Implement the SavingsAccount class


class CheckingAccount(Account):
    # Implement the CheckingAccount class


class Bank:
    # Implement the Bank class


# Test the implementation
bank = Bank()

while True:
    # Display menu options and get user input


    if choice == 1:
        # Prompt the user to create a new account


    elif choice == 2:
        # Prompt the user to make a deposit


    elif choice == 3:
        # Prompt the user to make a withdrawal


    elif choice == 4:
        # Prompt the user to view the account balance


    elif choice == 5:
        # Exit the program


    print("--------------------")
```

- Your task is to complete the implementation by following these instructions:

**Implement the log_transaction decorator function:**

- The decorator should log each transaction to a file named <account_number>.txt inside a folder named "transactions."

- Include the transaction type, account number, amount, and timestamp in the format: [timestamp]: Transaction Type: <transaction_type>, Account Number: <account_number>, Amount: <amount>.

- Create the "transactions" folder if it doesn't exist.

- Append the transaction log to the corresponding account's log file if it exists; otherwise, create a new file.

**Implement the Account class:**

- Implement the Account class with the required attributes and methods.

- Provide functionality for depositing and withdrawing funds.

- Include a method for retrieving the account balance.

- Implement the SavingsAccount and CheckingAccount classes:

- Implement the SavingsAccount and CheckingAccount classes as subclasses of Account.

- SavingsAccount should include functionality for earning interest on deposits.

- CheckingAccount should enforce a transaction limit.

**Implement the Bank class:**

- Implement the Bank class with methods for adding accounts.

- Include methods for retrieving accounts by account number and password.

- Add a method for getting the total balance across all accounts.

**Test the implementation by running the program:**

- The program should display a menu with the following options:

- Create Account: Prompt the user to enter a password, confirm the password, and select the account type (savings or checking). Collect the below details based on the account type. After successful account creation, display the account number to the user.

- Additional Details for Saving account
    - Interest rate
    - IFSC code
    - Joint account - Yes/No
- Additional Details for checking account
    - Minimum balance
    - IFSC code

- Deposit: Prompt the user to enter the account number, password, and deposit amount. If the account is valid, deposit the specified amount into the account and log the transaction.

- Withdraw: Prompt the user to enter the account number, password, and withdrawal amount. If the account is valid and has sufficient funds, withdraw the specified amount from the account and log the transaction.

- View Balance: Prompt the user to enter the account number and password. If the account is valid, display the current account balance.

- Exit: Terminate the program.

- Ensure proper error handling and display appropriate error messages for invalid inputs, insufficient funds, incorrect passwords, etc.

---

## Question 2:

**Sql test :**
*Instructions:*

- Import the given dump file into MySQL Workbench.
    - [File](./sql/sql_batch_training.sql)

- After importing, navigate to the "schemas" tab to find the "ecommerce" schema.

- Write SQL queries to retrieve specific details from the database.

*Questions:*

1. Find the late orders.

2. List orders from Paris placed between April 2003 to June 2003 along with their customer details.

3. Identify the top 5 customers who have made the highest purchases (generated the highest revenue).