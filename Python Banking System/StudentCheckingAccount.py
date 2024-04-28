from CheckingAccount import CheckingAccount

validSchools = ["Wilfrid Laurier", "University of Waterloo", "University of Toronto", "Toronto Metropolitan University"]

class StudentCheckingAccount(CheckingAccount):
    def __init__(self, accountNumber, accountHolderName, balance, bankType, school):
        super().__init__(accountNumber, accountHolderName, balance, bankType)
        self._school = school

    def atmWithdraw(self, amount, atmType):
        if self._school in validSchools:
            print("-Account type registered with valid school, fees ignored-")
            return super().atmWithdraw(amount, "Exception")
        else:
            return super().atmWithdraw(amount, atmType)

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print(f"Bank Type: {self._bankType}")
        print(f"School: {self._school}")
        print()