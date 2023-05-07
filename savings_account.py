from account import Account

class Savings_account(Account):

    def __init__(self):
        Account.__init__(self)
        self.interest = 10000
        self.withdraw_limit = 25000

    def withdraw(self, amount):
        if amount < self.withdraw_limit:
            self.account_balance = self.account_balance - amount
            print(self.account_balance)
        else:
            print("The amonut is more than the withdrawal limit")
save = Savings_account()
save.withdraw(20000)