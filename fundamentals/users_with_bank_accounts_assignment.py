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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0)
    def makeDeposit(self, amount):
        self.account.deposit(amount)
        return self
    def makeWithdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def displayBalance(self,):
        print(self.account.balance)




user1 = User("Grant", "gbrownzzzz58@gmail.com")
user1.makeDeposit(1000), user1.makeWithdraw(200), user1.displayBalance() 