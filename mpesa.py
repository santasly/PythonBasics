class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID {self.transaction_id} processed.Amount{self.amount}")


class WithrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withraw transaction with ID {self.transaction_id} processed. Amount{self.amount}")



class PaymentTransaction(MpesaTransaction):
#adding properties
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount)
        self.recepient = recepient

    def process_transaction(self):
        print(
            f"Payment transaction with ID{self.transaction_id} processed. Amount{self.amount}. Recepient{self.recepient}")

deposit = DepositTransaction("DHTY", 7000)
deposit.process_transaction()
withdrawal = WithrawalTransaction("WRYH", 4500)
withdrawal.process_transaction()
payment=PaymentTransaction("HGHK",1020,"eric")

