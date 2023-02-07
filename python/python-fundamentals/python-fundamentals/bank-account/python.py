class BankAccount:
    def __init__(self, int_rate:float, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if(self.balance < 0):
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        amount = self.balance * self.int_rate
        if(amount > 0):
            self.balance += amount
        return self