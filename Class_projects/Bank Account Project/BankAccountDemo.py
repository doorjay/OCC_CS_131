# Dorje Pradhan and Toan Tran
# December 5, 2022
# Python 1, CS 131
# Bank Account Project!

from BankAcount import * 

#Instantiate 3 objects
samsAcc = BankAccount(name = "Sam", type = "saving", balance = 100)
leilasAcc = BankAccount(name = "Leila", type = "saving", balance = 500)
adamsAcc = BankAccount(name = "Adam", type = "checking", balance = 100, interest = 0)

# adding interest to all three accounts
adamsAcc.addInterest()
samsAcc.addInterest()
leilasAcc.addInterest()

# using getBalance to print
print("Leila's balance after interest is $%.2f" % leilasAcc.getBalance())
print("Sam's balance after interest is $%.2f" % samsAcc.getBalance())
print("Adam's balance after interest is $%.2f" % adamsAcc.getBalance())

# testing exception with transfer more than balance amount
samsAcc.transfer(adamsAcc, 200)
leilasAcc.transfer(adamsAcc, 50)

# testing transfer and getName/getBalance
print("Adam's account balance after transfer is $%.2f" % adamsAcc.getBalance())
print("Leila's account balance after transfer is $%.2f" % leilasAcc.getBalance())

# testing deposit then printing after the deposit
adamsAcc.deposit(100)
samsAcc.deposit(100)
leilasAcc.deposit(100)

print("Leila's balance after deposit is $%.2f" %leilasAcc.getBalance())
print("Sam's balance after deposit is $%.2f" %samsAcc.getBalance())
print("Adam's balance after deposit is $%.2f" %adamsAcc.getBalance())


# testing withdrawal of more than account balance with Adam, then with Sam and Leila then printing Sam and Leila
adamsAcc.withdraw(300)
samsAcc.withdraw(200)
leilasAcc.withdraw(200)

print("Leila's balance after withdrawal is $%.2f" %leilasAcc.getBalance())
print("Sam's balance after withdrawal is $%.2f" %samsAcc.getBalance())

# tesing getAccNum and getAccountType
print("Adam account num:", adamsAcc.getAccNum())
print("Adam account type:", adamsAcc.getAccountType())

# display all account information after alterations for all 3 accounts
samsAcc.displayAccountInfo()
print()
leilasAcc.displayAccountInfo()
print()
adamsAcc.displayAccountInfo()