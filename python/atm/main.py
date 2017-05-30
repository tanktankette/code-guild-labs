import account
from os import system

def take_command():
    command = -1
    while command == -1:
        try:
            command = int(input("""
********Commands********
1: List Accounts
2: Open Account
3: Check Account
4: Deposit
5: Withdraw
6: Calculate Interest

0: Exit
************************
Input: """))
        except ValueError:
            system("clear")
            print("Error, not a valid input\n")
            continue
        system("clear")
        return command

bank = account.Bank()
command = -1

while command != 0:
    command = take_command()
    if command == 1:
        bank.get_accounts()
    if command == 2:
        bank.open_account()
    if command == 3:
        print(f"There is ${bank.get_funds(input('Account id: '))} in this account")
    if command == 4:
        bank.deposit(input("Account id: "), int(input("Amount: ")))
    if command == 5:
        bank.withdraw(input("Account id: "), int(input("Amount: ")))
    if command == 6:
        print(f"The interest would be ${bank.calc_interest(input('Account id: '))}")
