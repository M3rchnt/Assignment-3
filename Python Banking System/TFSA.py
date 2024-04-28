from SavingsAccount import SavingsAccount
class TFSA(SavingsAccount):
    def __init__(self, accountNumber, accountHolderName, balance, minimumBalance, interestRate, withdrawLimit, goal):
        super().__init__(accountNumber, accountHolderName, balance, minimumBalance, interestRate, withdrawLimit)
        self._goal = goal
        self._contributions = 0

    def deposit(self, amount):
        self._contributions += amount
        if self._contributions >= self._goal:
            print("Financial goal reached")
            newGoal = input("Please enter a new financial goal to work towards (> 0): ")
            if newGoal.isnumeric() and int(newGoal) > 0:
                self._goal = int(newGoal)
                self._contributions = 0
            else:
                while not newGoal.isnumeric() or int(newGoal) <= 0:
                    newGoal = input("Invalid input, please enter a new financial goal to work towards (> 0): ")
                self._goal = int(newGoal)
                self._contributions = 0
        return super().deposit(amount)

    def displayAccountDetails(self):
        print("Displaying information...")
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Name: {self._accountHolderName}")
        print(f"Account Balance: {self._balance}")
        print(f"Minimum Balance: {self._minimumBalance}")
        print(f"Interest Rate: {self._interestRate}")
        print(f"Withdraw Limit: {self._withdrawLimit}")
        print(f"Progress towards goal: {self._contributions}/{self._goal}")
        print()