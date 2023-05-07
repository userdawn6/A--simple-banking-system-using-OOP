from account import Account

class Current_account(Account):
    def __init__(self):
        Account.__init__(self)

current = Current_account()
current.deposite(30000)