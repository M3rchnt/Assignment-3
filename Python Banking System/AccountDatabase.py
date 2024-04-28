class AccountDatabase: 
    def __init__(self):
        self._accounts = []
    
    def add(self, account):
        check = self.checkIfAccountExists(account)
        if check == False:
            self._accounts.append(account)
        else:
            print("Error cannot create account, account number already exists")

    def remove(self, account):
        check = self.checkIfAccountExists(account)
        if check:
            self._accounts.remove(account)
        else:
            print("Account does not exist")
        return
    
    def removeAll(self):
        self._accounts = []
    
    def retrieveIndex(self, index):
        return self._accounts[index]

    def checkIfAccountExists(self, account):
        exists = False
        for i in self._accounts:
            if i._accountNumber == account._accountNumber:
                exists = True
        return exists
    
    def length(self):
        return len(self._accounts)