from SavingsAccount import SavingsAccount
class RRSP(SavingsAccount):
    def __init__(self, accountNumber, accountHolderName, balance, minimumBalance, interestRate, withdrawLimit, retired):
        super().__init__(accountNumber, accountHolderName, balance, minimumBalance, interestRate, withdrawLimit)
        self._retired = retired

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print(f"Minimum Balance: {self._minimumBalance}")
        print(f"Interest Rate: {self._interestRate}")
        print(f"Retired: {self._retired}")
        print()
    
    def withdraw(self, amount):
        if not self._retired:
            confirm = input("Withdrawing from the RRSP will incur 5% tax on the withdrawal, continue? (Y/N) ")
            match (confirm):
                case "Y":
                    return super().withdraw(int(amount*1.05))
                case "N":
                    print("Withdraw cancelled.")
                case default:
                    print("Unsupported action, please choose either Y or N")
            while confirm != "Y" and confirm != "N":
                confirm = input("Withdrawing from the RRSP will incur 5% tax on the withdrawal, continue? (Y/N) ")
                match (confirm):
                    case "Y":
                        return super().withdraw(int(amount*1.05))
                    case "N":
                        print("Withdraw cancelled.")
                    case default:
                        print("Unsupported action, please choose either Y or N")
        else:
            print("Retirement enabled, tax ignored")
            return super().withdraw(amount)