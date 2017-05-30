from random import randrange


class Account:
    def __init__(self, id_number, balance = 0, interest = 0.001):
        self._id_number = id_number
        self._balance = balance
        self._interest = interest

    def __str__(self):
        return f"{self._id_number}, {self._balance}, {self._interest}"

    def get_funds(self):
        return self._balance

    def deposit(self, amount):
        self.transaction_fee()
        self._balance += amount

    def check_withdrawal(self, amount):
        return amount <= self._balance

    def withdraw(self, amount):
        self.transaction_fee()
        if self.check_withdrawal(amount):
            self._balance -= amount
        else:
            raise ValueError

    def calc_interest(self):
        return self._balance * self._interest

    def get_standing(self):
        return self._balance < 1000

    def transaction_fee(self):
        if self.get_standing():
            self._balance -= 1
            print("$1 Transaction fee taken out")


class Bank:
    def __init__(self):
        self._accounts = {}
        self._load("bank.txt")

    def get_accounts(self):
        print("Opened accounts on file:")
        for a in self._accounts.keys():
            print(a)

    def open_account(self, id_number = 0, balance = 0, interest = 0.001):
        while id_number in self._accounts.keys() or id_number == 0:
            id_number = randrange(1,100)
        self._accounts[id_number] = Account(id_number, balance, interest)
        print(f"New account created with account id of {id_number}")
        self._save("bank.txt")

    def get_funds(self, id_number):
        if id_number in self._accounts.keys():
            return self._accounts[id_number].get_funds()

    def withdraw(self, id_number, amount):
        try:
            if id_number in self._accounts.keys():
                return self._accounts[id_number].withdraw(amount)
        except ValueError:
            print("Not enough money in account")
        self._save("bank.txt")

    def deposit(self, id_number, amount):
        if id_number in self._accounts.keys():
            return self._accounts[id_number].deposit(amount)
        self._save("bank.txt")

    def calc_interest(self, id_number):
        if id_number in self._accounts.keys():
            return self._accounts[id_number].calc_interest()

    def _save(self, file_name):
        opened_file = open(file_name,"w")
        for a in self._accounts.values():
            opened_file.write(str(a) + "\n")

    def _load(self, file_name):
        opened_file = open(file_name,"r")
        for a in opened_file:
            a = a.split(", ")
            self._accounts[a[0]] = Account(a[0],float(a[1]),float(a[2].strip("\n")))
