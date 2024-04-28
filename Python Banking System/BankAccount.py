class BankAccount:

    def __init__(self, accountNumber, accountHolderName, balance):
        assert balance >= 0, "Balance cannot be negative"
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if (self._balance >= amount):
            print("-Withdraw Succesful-")
            self._balance -= amount
        else:
            print("Insufficient funds")

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print()
