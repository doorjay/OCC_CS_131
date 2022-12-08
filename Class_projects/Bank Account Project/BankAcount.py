# Dorje Pradhan and Toan Tran
# December 5, 2022
# Python 1, CS 131
# Bank Account Project!

# default constructor-----------------------------
    # @param self
    # @param balance the bank account balance
    # @param type the type of the bank account
    # @param interest the interest
class BankAccount :
    _lastAccount = 1000

    def __init__(self, balance, name, type, interest = 0.03) :
        self._balance = balance
        self._accName = name
        self._accountType = type
        self._interestRate = interest

        # increase account number
        BankAccount._lastAccount += 1
        self._accNum = BankAccount._lastAccount

    # Accessor functions --------------------------------------------

    # @return : returns the current account balance 
    def getBalance(self):
        return self._balance

    # @return : returns the current account name
    def getName(self):
        return self._accName

    # @return : returns the current account type
    def getAccountType(self):
        return self._accountType

    # @return : returns the account number
    def getAccNum(self):
        return self._accNum

    # prints _accName, _accNum, _accType, and _balance
    def displayAccountInfo(self):
        print("The account name:", self.getName())
        print("The account num:", self.getAccNum())
        print("The account type:", self.getAccountType())
        print("The account balance: %.2f" % self.getBalance())

    # Mutator functions ---------------------------------------------

    # @param amount : the amount to remove from _balance
    def withdraw(self, amount) :
        try:
            if self._balance >= amount :
                self._balance -= amount
            else :
                raise ValueError

        except ValueError:
            print(self._accName, "has insufficient funds")
        

    # @param amount : the amount to add to _balance
    def deposite(self, amount) :
        self._balance += amount

    # @param otherAccount : am object of the BankAccount class
        # add money to this account
    # @param amount : the amount to take away from otherAccount 
    #                 and add to _blanace
    def transfer(self, otherAccount, amount) :
        self.withdraw(amount)
        otherAccount.deposite(amount)

    # adds money to _blance via compound interest
    def addInterest(self) :
        self._balance += Financial.percentOf(self._interestRate, self._balance)


class Financial :

    # @param interestRate : the interest rate
    # @param balance : the blance to calculate from
    # @return : the amount to add to BankAccount _balance
    @staticmethod
    def percentOf(interestRate, balance) :
        return interestRate * balance