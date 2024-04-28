from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, accountHolderName, balance, minimumBalance, interestRate, withdrawLimit):
        assert balance >= minimumBalance, "Initial balance must be greater than minimum balance"
        super().__init__(accountNumber, accountHolderName, balance)
        self._minimumBalance = minimumBalance
        self._interestRate = interestRate
        self._withdrawLimit = withdrawLimit

    def withdraw(self, amount):
        if (amount < self._withdrawLimit):
            if (self._balance - amount < self._minimumBalance):
                print("Withdraw denied, exceeds minimum balance")
            else:
                return super().withdraw(amount)
        else:
            print("Withdraw denied, exceeds withdraw limit")

    def applyInterest(self):
        self._balance = self._balance*(1+self._interestRate)
        print("-Interest rate applied-")

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print(f"Minimum Balance: {self._minimumBalance}")
        print(f"Interest Rate: {self._interestRate}")
        print(f"Withdraw Limit: {self._withdrawLimit}")
        print()