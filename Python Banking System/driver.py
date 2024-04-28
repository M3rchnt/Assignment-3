from SavingsAccount import SavingsAccount # Importing custom made classes
from CheckingAccount import CheckingAccount
from StudentCheckingAccount import StudentCheckingAccount
from StudentCheckingAccount import validSchools
from RRSP import RRSP
from TFSA import TFSA
from BankAccount import BankAccount
from AccountDatabase import AccountDatabase

def testBankAccount(): # Testing function for Bank Account, Base Account Containing Deposit, Withdraw and Display Info methods
    choice = "Y"
    while choice == "Y":
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        balance = input("Enter initial account balance (>= 0): ")
        while not balance.isnumeric() or int(balance) < 0:
            balance = input("Invalid input, Enter initial account balance (>= 0): ")
        account = BankAccount(accountNumber, accountName, int(balance))
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        pass

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return

def testSavingsAccount(): # Testing function for Savings Account, Child class of Bank Account, contains all parent methods and apply interest method which increments balance
    choice = "Y"          # Also overrides Withdraw to account for minimum balance check and Display Info method
    while choice == "Y":
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        minimumBalance = input("Enter account minimum balance (>= 0): ")
        while not minimumBalance.isnumeric() or int(minimumBalance) < 0:
            minimumBalance = input("Invalid input, Enter account minimum balance (>= 0): ")
        balance = input("Enter initial account balance (>= minimumBalance): ")
        while not balance.isnumeric() or int(balance) < int(minimumBalance):
            balance = input("Invalid input, Enter initial account balance (>= minimumBalance): ")
        interestRate = input("Enter interest rate (> 0 and < 1): ")
        while not interestRate.replace(".", "").isnumeric() or float(interestRate) < 0 or float(interestRate) > 1:
            interestRate = input("Invalid input, Enter interest rate (> 0 and < 1): ")
        withdrawLimit = input("Enter the withdraw limit for the account (> 0): ")
        while not withdrawLimit.isnumeric() or int(withdrawLimit) <= 0:
            withdrawLimit = input("Invalid input, Enter the withdraw limit for the account (> 0): ")
        account = SavingsAccount(accountNumber, accountName, int(balance), int(minimumBalance), float(interestRate), int(withdrawLimit))
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        pass

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 4. Apply Interest")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "4":
            account.applyInterest()
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 4. Apply Interest")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "4":
                account.applyInterest()
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return

def testCheckingAccount(): # Testing function for Checking Account, Child class of Bank Account, contains all parent methods and transferMoney method which transfers money from one account to another
    choice = "Y"           # Also contains atmWithdraw method which incurs a fee if the account isn't registered with the same bank type as the atm
    while choice == "Y":   # Overrides Display Info method
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        balance = input("Enter initial account balance (>= 0): ")
        while not balance.isnumeric() or int(balance) < 0:
            balance = input("Invalid input, Enter initial account balance (>= 0): ")
        bankType = input("Enter the name of the bank the account is being registered with: ")
        account = CheckingAccount(accountNumber, accountName, int(balance), bankType)
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        transferAccount = CheckingAccount(10015, "Test", 300, "TD")
        database.add(transferAccount)
    
        print()
        print("A spare account has been generated to test this function as some functions require multiple accounts")
        transferAccount.displayAccountDetails()
        print()

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 4. Transfer Money")
    print(" 5. atmWithdraw")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "4":
            newChoice = input(f"Enter which number account to transfer to (1 - {database.length()}): ")
            while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length}): ")
            transferAccount = database.retrieveIndex(int(newChoice)-1)
            transferAccount.displayAccountDetails()
            newChoice = input("Confirm choice? (Y/N): ")
            while newChoice != "Y" and newChoice != "N":
                newChoice = input("Invalid input, Confirm choice? (Y/N): ")
            while newChoice == "N":
                newChoice = input(f"Enter which number account to use (1 - {database.length()}): ")
                while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                    newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length()}): ")
                transferAccount = database.retrieveIndex(int(newChoice)-1)
                transferAccount.displayAccountDetails()
                newChoice = input("Confirm choice?:  (Y/N)")
                while newChoice != "Y" and newChoice != "N":
                    newChoice = input("Invalid input, Confirm choice? (Y/N): ")

            amount = input("Enter how much you would like to transfer (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to transfer (> 1): ")
            account.transferMoney(transferAccount, int(amount))
        case "5":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            atm = input("Enter the type of atm you are withdrawing from: ")
            account.atmWithdraw(int(amount), atm)
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 4. Transfer Money")
        print(" 5. atmWithdraw")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "4":
                newChoice = input(f"Enter which number account to transfer to (1 - {database.length()}): ")
                while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                    newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length}): ")
                transferAccount = database.retrieveIndex(int(newChoice)-1)
                transferAccount.displayAccountDetails()
                newChoice = input("Confirm choice? (Y/N): ")
                while newChoice != "Y" and newChoice != "N":
                    newChoice = input("Invalid input, Confirm choice? (Y/N): ")
                while newChoice == "N":
                    newChoice = input(f"Enter which number account to use (1 - {database.length()}): ")
                    while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                        newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length()}): ")
                    transferAccount = database.retrieveIndex(int(newChoice)-1)
                    transferAccount.displayAccountDetails()
                    newChoice = input("Confirm choice?:  (Y/N)")
                    while newChoice != "Y" and newChoice != "N":
                        newChoice = input("Invalid input, Confirm choice? (Y/N): ")

                amount = input("Enter how much you would like to transfer (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to transfer (> 1): ")
                account.transferMoney(transferAccount, int(amount))
            case "5":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                atm = input("Enter the type of atm you are withdrawing from: ")
                account.atmWithdraw(int(amount), atm)
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return

def testStudentCheckingAccount(): # Testing function for Student Checking Account, Child class of Checking Account, contains all parent methods and overrides atmWithdraw to cancel fees if school type is valid
    choice = "Y"                  # Also overrides Display Info method
    while choice == "Y":
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        balance = input("Enter initial account balance (>= 0): ")
        while not balance.isnumeric() or int(balance) < 0:
            balance = input("Invalid input, Enter initial account balance (>= 0): ")
        bankType = input("Enter the name of the bank the account is being registered with: ")
        print("List of Valid Schools: ", end="")
        for i in validSchools:
            print(f"{i}, ", end="")
        print()
        school = input("Enter the school the account is registered with: ")
        account = StudentCheckingAccount(accountNumber, accountName, int(balance), bankType, school)
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        transferAccount = StudentCheckingAccount(10015, "Test", 300, "TD", "Wilfrid Laurier")
        database.add(transferAccount)
    
        print()
        print("A spare account has been generated to test this function as some functions require multiple accounts")
        transferAccount.displayAccountDetails()
        print()

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 4. Transfer Money")
    print(" 5. atmWithdraw")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "4":
            newChoice = input(f"Enter which number account to transfer to (1 - {database.length()}): ")
            while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length}): ")
            transferAccount = database.retrieveIndex(int(newChoice)-1)
            transferAccount.displayAccountDetails()
            newChoice = input("Confirm choice? (Y/N): ")
            while newChoice != "Y" and newChoice != "N":
                newChoice = input("Invalid input, Confirm choice? (Y/N): ")
            while newChoice == "N":
                newChoice = input(f"Enter which number account to use (1 - {database.length()}): ")
                while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                    newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length()}): ")
                transferAccount = database.retrieveIndex(int(newChoice)-1)
                transferAccount.displayAccountDetails()
                newChoice = input("Confirm choice?:  (Y/N)")
                while newChoice != "Y" and newChoice != "N":
                    newChoice = input("Invalid input, Confirm choice? (Y/N): ")

            amount = input("Enter how much you would like to transfer (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to transfer (> 1): ")
            account.transferMoney(transferAccount, int(amount))
        case "5":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            atm = input("Enter the type of atm you are withdrawing from: ")
            account.atmWithdraw(int(amount), atm)
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 4. Transfer Money")
        print(" 5. atmWithdraw")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "4":
                newChoice = input(f"Enter which number account to transfer to (1 - {database.length()}): ")
                while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                    newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length}): ")
                transferAccount = database.retrieveIndex(int(newChoice)-1)
                transferAccount.displayAccountDetails()
                newChoice = input("Confirm choice? (Y/N): ")
                while newChoice != "Y" and newChoice != "N":
                    newChoice = input("Invalid input, Confirm choice? (Y/N): ")
                while newChoice == "N":
                    newChoice = input(f"Enter which number account to use (1 - {database.length()}): ")
                    while int(newChoice) < 1 or int(newChoice) > database.length() or not choice.isnumeric():
                        newChoice = input(f"Invalid input, Enter which number account to transfer to (1 - {database.length()}): ")
                    transferAccount = database.retrieveIndex(int(newChoice)-1)
                    transferAccount.displayAccountDetails()
                    newChoice = input("Confirm choice?:  (Y/N)")
                    while newChoice != "Y" and newChoice != "N":
                        newChoice = input("Invalid input, Confirm choice? (Y/N): ")

                amount = input("Enter how much you would like to transfer (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to transfer (> 1): ")
                account.transferMoney(transferAccount, int(amount))
            case "5":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                atm = input("Enter the type of atm you are withdrawing from: ")
                account.atmWithdraw(int(amount), atm)
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return

def testRRSP(): # Testing function for RRSP, Child class of Savings Account, contains all parent methods and check for retirement which applies fees when withdrawing if retirement is not yet reached
    choice = "Y"# Also overrides Display Info method
    while choice == "Y":
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        minimumBalance = input("Enter account minimum balance (>= 0): ")
        while not minimumBalance.isnumeric() or int(minimumBalance) < 0:
            minimumBalance = input("Invalid input, Enter account minimum balance (>= 0): ")
        balance = input("Enter initial account balance (>= minimumBalance): ")
        while not balance.isnumeric() or int(balance) < int(minimumBalance):
            balance = input("Invalid input, Enter initial account balance (>= minimumBalance): ")
        interestRate = input("Enter interest rate (> 0 and < 1): ")
        while not interestRate.replace(".", "").isnumeric() or float(interestRate) < 0 or float(interestRate) > 1:
            interestRate = input("Invalid input, Enter interest rate (> 0 and < 1): ")
        withdrawLimit = input("Enter the withdraw limit for the account (> 0): ")
        while not withdrawLimit.isnumeric() or int(withdrawLimit) <= 0:
            withdrawLimit = input("Invalid input, Enter the withdraw limit for the account (> 0): ")
        retired = input("Enter if the account has reached retirement (T/F): ")
        while retired != "T" and retired != "F":
            retired = input("Invalid input, Enter if the account has reached retirement (T/F): ")
        if retired == "T":
            retired = True
        else:
            retired = False
        account = RRSP(accountNumber, accountName, int(balance), int(minimumBalance), float(interestRate), int(withdrawLimit), retired)
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        pass

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 4. Apply Interest")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "4":
            account.applyInterest()
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 4. Apply Interest")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "4":
                account.applyInterest()
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return

def testTFSA(): # Testing function for TFSA, Child class of Savings Account, contains all parent methods and goal variable to check if the account has reached the savings goal
    choice = "Y"# Overrides Display Info method as well as deposit method to adjust the contributions made towards the savings goal.
    while choice == "Y":
        accountNumber = input("Enter an account number: ")
        while not accountNumber.isnumeric():
            accountNumber = input("Invalid input, Enter an account number: ")
        accountName = input("Enter account name: ")
        minimumBalance = input("Enter account minimum balance (>= 0): ")
        while not minimumBalance.isnumeric() or int(minimumBalance) < 0:
            minimumBalance = input("Invalid input, Enter account minimum balance (>= 0): ")
        balance = input("Enter initial account balance (>= minimumBalance): ")
        while not balance.isnumeric() or int(balance) < int(minimumBalance):
            balance = input("Invalid input, Enter initial account balance (>= minimumBalance): ")
        interestRate = input("Enter interest rate (> 0 and < 1): ")
        while not interestRate.replace(".", "").isnumeric() or float(interestRate) < 0 or float(interestRate) > 1:
            interestRate = input("Invalid input, Enter interest rate (> 0 and < 1): ")
        withdrawLimit = input("Enter the withdraw limit for the account (> 0): ")
        while not withdrawLimit.isnumeric() or int(withdrawLimit) <= 0:
            withdrawLimit = input("Invalid input, Enter the withdraw limit for the account (> 0): ")
        goal = input("Enter a monetary savings goal to work towards (> 0): ")
        while not goal.isnumeric() or int(goal) <= 0:
            goal = input("Invalid input, Enter a monetary savings goal to work towards (> 0): ")
        account = TFSA(accountNumber, accountName, int(balance), int(minimumBalance), float(interestRate), int(withdrawLimit), int(goal))
        database.add(account)
        choice = input("Enter another account? (Y/N) ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Enter another account? (Y/N) ")

    if database.length() > 1:
        choice = input(f"Enter which number account to use (1 - {database.length()}): ")
        while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
            choice = input(f"Invalid input, Enter which number account to use (1 - {database.length}): ")
        account = database.retrieveIndex(int(choice)-1)
        account.displayAccountDetails()
        choice = input("Confirm choice? (Y/N): ")
        while choice != "Y" and choice != "N":
            choice = input("Invalid input, Confirm choice? (Y/N): ")
        while choice == "Y":
            choice = input(f"Enter which number account to use (1 - {database.length()}): ")
            while int(choice) < 1 or int(choice) > database.length() or not choice.isnumeric():
                choice = input(f"Invalid input, Enter which number account to use (1 - {database.length()}): ")
            account = database.retrieveIndex(int(choice)-1)
            account.displayAccountDetails()
            choice = input("Confirm choice?:  (Y/N)")
            while choice != "Y" and choice != "N":
                choice = input("Invalid input, Confirm choice? (Y/N): ")
    elif database.length() == 1:
        pass

    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Display Account Details")
    print(" 4. Apply Interest")
    print(" 0. Exit Function")

    choice = input("Select an option to use: ")
    match (choice):
        case "1":
            amount = input("Enter how much you would like to deposit (> 1): ")
            while not amount.isnumeric or int(amount) < 1:
                amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
            account.deposit(int(amount))
        case "2":
            amount = input("Enter how much you would like to withdraw (> 0): ")
            while not amount.isnumeric or int(amount) < 0: 
                amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
            account.withdraw(int(amount))
        case "3":
            account.displayAccountDetails()
        case "4":
            account.applyInterest()
        case "0":
            pass
        case default:
            print("Invalid input")
    while choice != "0":
        print(" 1. Deposit")
        print(" 2. Withdraw")
        print(" 3. Display Account Details")
        print(" 4. Apply Interest")
        print(" 0. Exit Function")

        choice = input("Select an option to use: ")
        match (choice):
            case "1":
                amount = input("Enter how much you would like to deposit (> 1): ")
                while not amount.isnumeric or int(amount) < 1:
                    amount = input("Invalid input, Enter how much you would like to deposit (> 1): ")
                account.deposit(int(amount))
            case "2":
                amount = input("Enter how much you would like to withdraw (> 0): ")
                while not amount.isnumeric or int(amount) < 0: 
                    amount = input("Invalid input, Enter how much you would like to withdraw (> 0): ")
                account.withdraw(int(amount))
            case "3":
                account.displayAccountDetails()
            case "4":
                account.applyInterest()
            case "0":
                pass
            case default:
                print("Invalid input")
    database.removeAll()
    return 

database = AccountDatabase()
print(" 1. Bank Account")
print(" 2. Savings Account")
print(" 3. Checking Account")
print(" 4. Student Checking Account")
print(" 5. RRSP")
print(" 6. TFSA")
print(" 0. Exit Program")
choice = input("Which back account would you like to create? ")
while choice != "0":
    match (choice):
        case "1":
            testBankAccount()
        case "2":
            testSavingsAccount()
        case "3":
            testCheckingAccount()
        case "4":
            testStudentCheckingAccount()
        case "5":
            testRRSP()
        case "6":
            testTFSA()
        case "0":
            print("Exiting program")
        case default:
            print("Invalid input")
    print(" 1. Bank Account")
    print(" 2. Savings Account")
    print(" 3. Checking Account")
    print(" 4. Student Checking Account")
    print(" 5. RRSP")
    print(" 6. TFSA")
    print(" 0. Exit Program")
    choice = input("Which back account would you like to create? ")
