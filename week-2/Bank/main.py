from bank import Bank

try:
    bank = Bank()
except Exception as e:
    print(f"Error occurred:{e}")
    
while True:
    menu = """Welcome to ABC Bank!\nPlease select an option!\n1.Create Account\n2.Deposit funds\n3.Withdraw Funds\n4.View Balance\n5.Exit
    """
    print(menu)
    try:
        choice = int(input("Enter a option:"))
        match choice:
            case 1:
                # Prompt the user to create a new account
                account_type = input("Enter account type (savings(s)/checking(c)): ").lower()
                password = input("Enter a password: ")
                confirm_password = input("Confirm password: ")

                if password != confirm_password:
                    print("Passwords do not match.")
                    print("--------------------")
                    continue
                try:
                    if account_type == "savings" or account_type.startswith("s"):
                        account_type = "savings"
                        interest_rate = float(input("Enter interest rate: "))
                        ifsc_code = input("Enter IFSC code: ")
                        joint_account = input("Is this a joint account? (yes/no): ").lower() == "no"
                        account_number = bank.create_account(account_type, password, interest_rate, ifsc_code, joint_account)
                    elif account_type == "checking" or account_type.startswith("c"):
                        account_type = "checking"
                        min_balance = float(input("Enter minimum balance: "))
                        ifsc_code = input("Enter IFSC code: ")
                        account_number = bank.create_account(account_type, password, min_balance, ifsc_code)
                    else:
                        raise ValueError()
                except ValueError as ve:
                    print("Incorrect Option for account type!")
                    print("---------------------------------")
                    continue
                                    
                print(f"Account created successfully. Your account number is {account_number}")
            
            case 2:
                # Prompt the user to make a deposit
                account_number = input("Enter your account number: ")
                password = input("Enter your password: ")
                amount = float(input("Enter deposit amount: "))

                account = bank.get_account(account_number, password)
                if account:
                    account.deposit(amount)
                else:
                    print("Invalid account number or password.")
                    print("--------------------")
            
            case 3:
                # Prompt the user to make a withdrawal
                account_number = input("Enter your account number: ")
                password = input("Enter your password: ")
                amount = float(input("Enter withdrawal amount: "))

                account = bank.get_account(account_number, password)
                if account:
                    account.withdraw(amount)
                else:
                    print("Invalid account number or password.")
                    print("--------------------")
            
            case 4:
                # Prompt the user to view the account balance
                account_number = input("Enter your account number: ")
                password = input("Enter your password: ")

                account = bank.get_account(account_number, password)
                if account:
                    print(f"Your current balance is {account.get_balance()}")
                else:
                    print("Invalid account number or password.")
                    print("--------------------")
            
            case 5:
                # Exit the program
                print("Exiting the program.")
                break
            
            case _:
                # Invalid type
                print("Invalid Option! Choose another Option!")
                print("--------------------")
                continue
    except (ValueError) as ve:
        print(f"Value Error Occurred!")
        print("--------------------")
        continue
    except Exception as e:
        print(f"Exception occurred! {e}")
    print("--------------------")