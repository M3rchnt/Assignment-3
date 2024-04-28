from BankAccount import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, accountHolderName, balance, bankType):
        super().__init__(accountNumber, accountHolderName, balance)
        self._bankType = bankType

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print(f"Bank Type: {self._bankType}")
        print()

    def transferMoney(self, targetAccount, amount):
        if isinstance(targetAccount, CheckingAccount):
            if (self._balance - amount >= 0):
                self._balance -= amount
                targetAccount._balance += amount
                print("Transfer success")
            else:
                print("Insufficient funds to conduct transfer")
        else:
            print("Target account is not checking account, cannot transfer money")

    def atmWithdraw(self, amount, atmType):
        assert atmType != "", "ATM type cannot be empty"
        if atmType != self._bankType and atmType != "Exception": 
            confirm = input("Fee incurred of 20$, continue with withdrawal? (Y/N)")
            match (confirm):
                case "Y":
                    if (self._balance - (amount+20) >= 0):
                        self._balance -= (amount + 20)
                    else:
                        print("Insufficient funds to conduct withdrawal and pay fee")
                case "N":
                    print("Withdraw cancelled.")
                case default:
                    print("Unsupported action, please choose either Y or N")
            while confirm != "Y" and confirm != "N":
                confirm = input("Fee incurred of 20$, continue with withdrawal? (Y/N)")
                match (confirm):
                    case "Y":
                        if (self._balance - (amount+20) >= 0):
                            self._balance -= (amount + 20)
                        else:
                            print("Insufficient funds to conduct withdrawal and pay fee")
                    case "N":
                        print("Withdraw cancelled.")
                    case default:
                        print("Unsupported action, please choose either Y or N")
        else:
            print("Matching back type or exception allowed, no fees incurred...")
            if (self._balance - amount >= 0):
                self._balance -= amount
            else:
                print("Insufficient funds to conduct withdrawal and pay fee")