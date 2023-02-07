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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0), BankAccount(int_rate=0.02, balance=0)]

    def make_deposit(self, account_id, amount):
        self.account[account_id].deposit(amount)
        self.display_user_balance(account_id)

    def make_withdrawal(self, account_id, amount):
        self.account[account_id].withdraw(amount)
        self.display_user_balance(account_id)

    def display_user_balance(self, account_id):
        print(f"{self.name}'s Balance: {self.account[account_id].balance}")

    def transfer_money(self, amount, account_id, other_user, other_user_account_id):
        if(other_user != None):
            self.make_withdrawal(account_id, amount)
            other_user.make_deposit(other_user_account_id, amount)
        else:
            print("That user is invalid.")

user1 = User("Reece", "reece@mail.com")
user2 = User("Hunter", "hunter@mail.com")

user1.make_deposit(0, 300)
# user1.make_withdrawal(0, 100)

user1.transfer_money(100, 0, user2, 0)