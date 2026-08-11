class Account:
    def __init__(self, acc_number, name, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount positive hona chahiye")
        self.__balance += amount
        log_transaction(self.acc_number, "Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount positive hona chahiye")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        log_transaction(self.acc_number, "Withdraw", amount)

    def display(self):
        print(f"Account No: {self.acc_number} | Name: {self.name} | Balance: {self.__balance}")


def save_account(account):
    with open("accounts.txt", "a") as f:
        f.write(f"{account.acc_number},{account.name},{account.get_balance()}\n")

def update_accounts_file(accounts):
    with open("accounts.txt", "w") as f:
        for acc in accounts.values():
            f.write(f"{acc.acc_number},{acc.name},{acc.get_balance()}\n")

def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as f:
            for line in f:
                acc_number, name, balance = line.strip().split(",")
                accounts[acc_number] = Account(acc_number, name, float(balance))
    except FileNotFoundError:
        pass
    return accounts


def log_transaction(acc_number, trans_type, amount):
    with open("transactions.txt", "a") as f:
        f.write(f"Account: {acc_number} | Type: {trans_type} | Amount: {amount}\n")


def main():
    accounts = load_accounts()

    while True:
        print("\n----- BANK MANAGEMENT SYSTEM -----")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                acc_number = input("Enter new account number: ")
                if acc_number in accounts:
                    print("Error: Account number already exists!")
                    continue
                name = input("Enter account holder name: ")
                new_acc = Account(acc_number, name)
                accounts[acc_number] = new_acc
                save_account(new_acc)
                print("Account created successfully!")

            elif choice == "2":
                acc_number = input("Enter account number: ")
                if acc_number not in accounts:
                    raise KeyError("Account not found")
                amount = float(input("Enter deposit amount: "))
                accounts[acc_number].deposit(amount)
                update_accounts_file(accounts)
                print("Deposit successful!")

            elif choice == "3":
                acc_number = input("Enter account number: ")
                if acc_number not in accounts:
                    raise KeyError("Account not found")
                amount = float(input("Enter withdraw amount: "))
                accounts[acc_number].withdraw(amount)
                update_accounts_file(accounts)
                print("Withdrawal successful!")

            elif choice == "4":
                acc_number = input("Enter account number: ")
                if acc_number not in accounts:
                    raise KeyError("Account not found")
                print(f"Balance: {accounts[acc_number].get_balance()}")

            elif choice == "5":
                acc_number = input("Enter account number: ")
                if acc_number not in accounts:
                    raise KeyError("Account not found")
                accounts[acc_number].display()

            elif choice == "6":
                print("Thank you for using our Bank System!")
                break

            else:
                print("Invalid choice! Please select 1-6.")

        except ValueError as e:
             print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()