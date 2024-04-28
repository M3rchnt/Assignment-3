package com.example;
import java.util.Scanner;


public final class driver {
    
    public static void main(String[] args) {
        System.out.println(" 1. Bank Account");
        System.out.println(" 2. Savings Account");
        System.out.println(" 3. Checking Account");
        System.out.println(" 4. Student Checking Account");
        System.out.println(" 5. RRSP");
        System.out.println(" 6. TFSA");
        System.out.println(" 0. Exit Program");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Which bank account would you like to create? ");
        String choice = scanner.nextLine();
        while (choice.compareTo("0") != 0) {
            switch (choice) {
                case "1":
                    Helper.testBankAccount();
                    break;
                case "2":
                    Helper.testSavingsAccount();
                    break;
                case "3":
                    Helper.testCheckingAccount();
                    break;
                case "4":
                    Helper.testStudentCheckingAccount();
                    break;
                case "5":
                    Helper.testRRSP();
                    break;
                case "6":
                    Helper.testTFSA();
                    break;
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            System.out.println(" 1. Bank Account");
            System.out.println(" 2. Savings Account");
            System.out.println(" 3. Checking Account");
            System.out.println(" 4. Student Checking Account");
            System.out.println(" 5. RRSP");
            System.out.println(" 6. TFSA");
            System.out.println(" 0. Exit Program");
            System.out.println("Which bank account would you like to create? ");
            choice = scanner.nextLine();
        }
        scanner.close();
    }
}

class Helper {
    public static void testBankAccount() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter initial account balance (>= 0)");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0) {
                System.out.println("Enter initial account balance (>= 0)");
                balance = scanner.nextLine();
            }
            BankAccount account = new BankAccount(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance));

            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }

    public static void testSavingsAccount() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter account minimum balance (>= 0): ");
            String minimumBalance = scanner.nextLine();
            while (Integer.parseInt(minimumBalance) < 0) {
                System.out.println("Enter account minimum balance (>= 0)");
                minimumBalance = scanner.nextLine();
            }
            System.out.println("Enter initial account balance (>= 0): ");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0 && Integer.parseInt(balance) < Integer.parseInt(minimumBalance)) {
                System.out.println("Enter initial account balance (>= 0): ");
                balance = scanner.nextLine();
            }
            System.out.println("Enter interest rate (> 0 and < 1): ");
            String interestRate = scanner.nextLine();
            while (Float.parseFloat(interestRate) > 1 && Float.parseFloat(interestRate) < 0) {
                System.out.println("Enter interest rate (> 0 and < 1): ");
                interestRate = scanner.nextLine();
            }
            System.out.println("Enter the withdraw limit for the account (> 0): ");
            String withdrawLimit = scanner.nextLine();
            while (Integer.parseInt(withdrawLimit) < 0) {
                System.out.println("Enter the withdraw limit for the account (> 0): ");
                withdrawLimit = scanner.nextLine();
            }
            SavingsAccount account = new SavingsAccount(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance), Integer.parseInt(minimumBalance), Float.parseFloat(interestRate), Integer.parseInt(withdrawLimit));

            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 4. Apply Interest");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "4":
                    account.applyInterest();
                    break; 
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 4. Apply Interest");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "4":
                        account.applyInterest();
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }

    public static void testCheckingAccount() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter initial account balance (>= 0)");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0) {
                System.out.println("Enter initial account balance (>= 0)");
                balance = scanner.nextLine();
            }
            System.out.println("Enter the name of the bank the account is being registered with: ");
            String bankType = scanner.nextLine();
            CheckingAccount account = new CheckingAccount(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance), bankType);
            CheckingAccount account2 = new CheckingAccount(10025, "Test", 200, "TD");
            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 4. Transfer Money");
            System.out.println(" 5. atmWithdraw");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "4":
                    System.out.println("Enter how much you would like to transfer (> 1): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) < 1) {
                        System.out.println("Invalid input, Enter how much you would like to transfer (> 1): ");
                        amount = scanner.nextLine();
                    }
                    account.transferMoney(account2, Integer.parseInt(amount));
                    account2.displayAccountDetails();
                    break;
                case "5":
                    System.out.println("Enter how much you would like to withdraw (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) < 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    System.out.println("Enter the type of atm you are withdrawing from: ");
                    String atm = scanner.nextLine();
                    account.atmWithdraw(Integer.parseInt(amount), atm);
                    break;
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 4. Transfer Money");
                System.out.println(" 5. atmWithdraw");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "4":
                        System.out.println("Enter how much you would like to transfer (> 1): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) < 1) {
                            System.out.println("Invalid input, Enter how much you would like to transfer (> 1): ");
                            amount = scanner.nextLine();
                        }
                        account.transferMoney(account2, Integer.parseInt(amount));
                        account2.displayAccountDetails();
                        break;
                    case "5":
                        System.out.println("Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) < 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        System.out.println("Enter the type of atm you are withdrawing from: ");
                        String atm = scanner.nextLine();
                        account.atmWithdraw(Integer.parseInt(amount), atm);
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }

    public static void testStudentCheckingAccount() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter initial account balance (>= 0)");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0) {
                System.out.println("Enter initial account balance (>= 0)");
                balance = scanner.nextLine();
            }
            System.out.println("Enter the name of the bank the account is being registered with: ");
            String bankType = scanner.nextLine();
            System.out.println("List of Valid Schools: ");
            for (String i : StudentCheckingAccount.validSchools) {
                System.out.print(i + ", ");
            }
            System.out.println();
            System.out.println("Enter the school the account is registered with: ");
            String school = scanner.nextLine();
            StudentCheckingAccount account = new StudentCheckingAccount(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance), bankType, school);
            StudentCheckingAccount account2 = new StudentCheckingAccount(10025, "Test", 200, "TD", "Wilfrid Laurier");
            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 4. Transfer Money");
            System.out.println(" 5. atmWithdraw");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "4":
                    System.out.println("Enter how much you would like to transfer (> 1): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) < 1) {
                        System.out.println("Invalid input, Enter how much you would like to transfer (> 1): ");
                        amount = scanner.nextLine();
                    }
                    account.transferMoney(account2, Integer.parseInt(amount));
                    account2.displayAccountDetails();
                    break;
                case "5":
                    System.out.println("Enter how much you would like to withdraw (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) < 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    System.out.println("Enter the type of atm you are withdrawing from: ");
                    String atm = scanner.nextLine();
                    account.atmWithdraw(Integer.parseInt(amount), atm);
                    break;
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 4. Transfer Money");
                System.out.println(" 5. atmWithdraw");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "4":
                        System.out.println("Enter how much you would like to transfer (> 1): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) < 1) {
                            System.out.println("Invalid input, Enter how much you would like to transfer (> 1): ");
                            amount = scanner.nextLine();
                        }
                        account.transferMoney(account2, Integer.parseInt(amount));
                        account2.displayAccountDetails();
                        break;
                    case "5":
                        System.out.println("Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) < 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        System.out.println("Enter the type of atm you are withdrawing from: ");
                        String atm = scanner.nextLine();
                        account.atmWithdraw(Integer.parseInt(amount), atm);
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }

    public static void testRRSP() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter account minimum balance (>= 0): ");
            String minimumBalance = scanner.nextLine();
            while (Integer.parseInt(minimumBalance) < 0) {
                System.out.println("Enter account minimum balance (>= 0)");
                minimumBalance = scanner.nextLine();
            }
            System.out.println("Enter initial account balance (>= 0): ");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0 && Integer.parseInt(balance) < Integer.parseInt(minimumBalance)) {
                System.out.println("Enter initial account balance (>= 0): ");
                balance = scanner.nextLine();
            }
            System.out.println("Enter interest rate (> 0 and < 1): ");
            String interestRate = scanner.nextLine();
            while (Float.parseFloat(interestRate) > 1 && Float.parseFloat(interestRate) < 0) {
                System.out.println("Enter interest rate (> 0 and < 1): ");
                interestRate = scanner.nextLine();
            }
            System.out.println("Enter the withdraw limit for the account (> 0): ");
            String withdrawLimit = scanner.nextLine();
            while (Integer.parseInt(withdrawLimit) < 0) {
                System.out.println("Enter the withdraw limit for the account (> 0): ");
                withdrawLimit = scanner.nextLine();
            }
            System.out.println("Enter if the account has reached retirement (T/F): ");
            String retired = scanner.nextLine();
            boolean boolRetired;
            if (retired.compareTo("T") == 0) {
                boolRetired = true;
            }
            else {
                boolRetired = false;
            }
            RRSP account = new RRSP(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance), Integer.parseInt(minimumBalance), Float.parseFloat(interestRate), Integer.parseInt(withdrawLimit), boolRetired);

            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 4. Apply Interest");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "4":
                    account.applyInterest();
                    break; 
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 4. Apply Interest");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "4":
                        account.applyInterest();
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }

    public static void testTFSA() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Enter an account number: ");
            String accountNumber = scanner.nextLine();
            System.out.println("Enter account name: ");
            String accountName = scanner.nextLine();
            System.out.println("Enter account minimum balance (>= 0): ");
            String minimumBalance = scanner.nextLine();
            while (Integer.parseInt(minimumBalance) < 0) {
                System.out.println("Enter account minimum balance (>= 0)");
                minimumBalance = scanner.nextLine();
            }
            System.out.println("Enter initial account balance (>= 0): ");
            String balance = scanner.nextLine();
            while (Integer.parseInt(balance) < 0 && Integer.parseInt(balance) < Integer.parseInt(minimumBalance)) {
                System.out.println("Enter initial account balance (>= 0): ");
                balance = scanner.nextLine();
            }
            System.out.println("Enter interest rate (> 0 and < 1): ");
            String interestRate = scanner.nextLine();
            while (Float.parseFloat(interestRate) > 1 && Float.parseFloat(interestRate) < 0) {
                System.out.println("Enter interest rate (> 0 and < 1): ");
                interestRate = scanner.nextLine();
            }
            System.out.println("Enter the withdraw limit for the account (> 0): ");
            String withdrawLimit = scanner.nextLine();
            while (Integer.parseInt(withdrawLimit) < 0) {
                System.out.println("Enter the withdraw limit for the account (> 0): ");
                withdrawLimit = scanner.nextLine();
            }
            System.out.println("Enter a monetary savings goal to work towards (> 0): ");
            String goal = scanner.nextLine();
            while (Integer.parseInt(goal) <= 0) {
                System.out.println("Invalid input, Enter a monetary savings goal to work towards (> 0): ");
                goal = scanner.nextLine();
            }
            TFSA account = new TFSA(Integer.parseInt(accountNumber), accountName, Integer.parseInt(balance), Integer.parseInt(minimumBalance), Float.parseFloat(interestRate), Integer.parseInt(withdrawLimit), Integer.parseInt(goal));

            System.out.println(" 1. Deposit");
            System.out.println(" 2. Withdraw");
            System.out.println(" 3. Display Account Details");
            System.out.println(" 4. Apply Interest");
            System.out.println(" 0. Exit Function\n");
            System.out.println("Select an option to use: ");
            String choice = scanner.nextLine();
            String amount;
            switch (choice) {
                case "1":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.deposit(Integer.parseInt(amount));
                    break;
                case "2":
                    System.out.println("Enter how much you would like to deposit (> 0): ");
                    amount = scanner.nextLine();
                    while (Integer.parseInt(amount) <= 0) {
                        System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                        amount = scanner.nextLine();
                    }
                    account.withdraw(Integer.parseInt(amount));
                    break;
                case "3":
                    account.displayAccountDetails();
                    break;
                case "4":
                    account.applyInterest();
                    break; 
                case "0":
                    break;
                default:
                    System.out.println("Invalid input");
            }
            while (choice.compareTo("0") != 0) {
                System.out.println(" 1. Deposit");
                System.out.println(" 2. Withdraw");
                System.out.println(" 3. Display Account Details");
                System.out.println(" 4. Apply Interest");
                System.out.println(" 0. Exit Function\n");
                System.out.println("Select an option to use: ");
                choice = scanner.nextLine();
                switch (choice) {
                    case "1":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to deposit (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.deposit(Integer.parseInt(amount));
                        break;
                    case "2":
                        System.out.println("Enter how much you would like to deposit (> 0): ");
                        amount = scanner.nextLine();
                        while (Integer.parseInt(amount) <= 0) {
                            System.out.println("Invalid input, Enter how much you would like to withdraw (> 0): ");
                            amount = scanner.nextLine();
                        }
                        account.withdraw(Integer.parseInt(amount));
                        break;
                    case "3":
                        account.displayAccountDetails();
                        break;
                    case "4":
                        account.applyInterest();
                        break;
                    case "0":
                        break;
                    default:
                        System.out.println("Invalid input");
                }
            }

        }
        catch (NumberFormatException e) {
            System.out.println("Invalid number input");
        }
        scanner.close();
    }
}