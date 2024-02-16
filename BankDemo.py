class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello "+self.cname+", Your Account Number "+str(self.acno)+" Is Opened With "+str(self.balance)+" Rs.")
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("You Need Another "+str(amount-self.balance)+" Rs.")
    def chekcBalance(self):
        print("Your Current Balance Is : "+str(self.balance))

b1=Bank()
acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance : "))

b1.openAccount(acno,cname,balance)

while True:

    print("*"*60)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*60)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)
    elif choice==3:
        b1.chekcBalance()
    elif choice==4:
        print("Thank You For Using Our Services.")
        print("*"*60)
        break
    else:
        print("Invalid Choice. Please Try Again")
        print("*"*60)
        
