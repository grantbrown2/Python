class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.interest = 0.03
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough funds, you have been charged 5$!")
            self.balance -= 5
            return
        self.balance -= amount
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        print("---After interest---")
        if self.balance > 0:
            self.balance += (self.balance * self.interest)

print("---User 1 Bank Account Information---")
User1 = BankAccount(0)
User1.deposit(50)
User1.withdraw(5)
User1.display_account_info()
User1.yield_interest()
User1.display_account_info()

print("---User 2 Bank Account Information---")
User2 = BankAccount(0)
User2.deposit(100), User2.withdraw(25), User2.withdraw(50), User2.withdraw(15), User2.display_account_info(), User2.yield_interest(), User2.display_account_info()

print("---Grant's Bank Account Information---")
grant = BankAccount(0)
grant.deposit(500), grant.deposit(250), grant.withdraw(25), grant.withdraw(120), grant.withdraw(100), grant.withdraw(28), grant.display_account_info(), grant.yield_interest(), grant.display_account_info()