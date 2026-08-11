# Bank Management System

A console-based Bank Management System built in Python, demonstrating core Object-Oriented Programming, Exception Handling, and File Handling concepts.

## Features
- Create a new bank account
- Deposit money into an account
- Withdraw money from an account
- Check account balance
- Display account details
- Persistent storage of account and transaction data using file handling

## Concepts Used
- **OOP:** Classes, objects, constructors, methods, and encapsulation (private balance attribute)
- **Exception Handling:** Handles invalid account numbers, invalid amounts, insufficient balance, account not found, invalid input, and file-related errors
- **File Handling:** Account details stored in `accounts.txt`, transaction history stored in `transactions.txt`

## How to Run
1. Clone this repository
2. Navigate to the project folder:
cd BankManagementSystem
3. Run the program:
python bank.py
## Main File
- `bank.py` — contains all program logic
- `accounts.txt` — stores account records
- `transactions.txt` — stores transaction history