class Account:
    def __init__(self, name, balance, min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance+=amount

    def withdrawl(self,amount):
        if self.balance>=self.min_balance:
            self.balance-=amount
        else:
            print('''sorry u don't have enough funds''')

    def statement(self):
        print('Account balance is {}'.format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return '''{}'s current has rs{} balance'''.format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)
