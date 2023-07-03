class BankAccount:
    def __init__(self,account_number, holder_name, balances=0):
        self.Acc_number=account_number
        self.hldr_name=holder_name
        self.bal=balances
    def deposit(self, amount):
        self.bal +=amount
    def withdraw(self,amount):
        if self.bal>=amount:
            self.bal-=amount
        else:
            print("insufficient funds")
    def display_balance(self):
        print(f"Account Number:{self.Acc_number}")
        print(f"Holder Name:{self.hldr_name}")
        print(f"Balance :{self.bal}")

my_account=BankAccount( "122354", "Jane", 1000)
my_account.display_balance()
my_account.withdraw(200)
my_account.display_balance()
my_account.deposit(500)
my_account.display_balance()