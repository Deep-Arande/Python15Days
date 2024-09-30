# Implement a program that simulates a basic bank account
# using a BankAccount class


class BankAccount:

    def __init__(self, name, initial_balance):#constructor

        self.name = name
        self.balance = initial_balance

    def deposit(self, amount): #function to deposit amount

        if (amount >= 0):

            self.balance += amount
            print(f"The amount of {amount} is added successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):#function to withdraw money

        if (amount > self.balance):
            print(f"Insufficient balance")

        elif (amount <= self.balance and amount >= 0):
            self.balance-=amount
            print(f"The amount {amount} was withdrawn successfully.")

        else:
            print("Withdrawal amount must be positive")

    def check_balance(self): #function to check balance

        print(f"Your current balance is {self.balance}")


name=str(input("Enter your name: "))
sum=int(input("Enter your initial amount: "))


customer=BankAccount(name,sum)


while(True):
    
    print("\nTo deposit: 1")
    print("To withdraw: 2")
    print("To check balance: 3")
    print("To exit: 4")
    
    n=int(input("Enter your choice: "))
    
    if(n==1):
        deposit=int(input("Enter the amount to deposit: "))
        customer.deposit(deposit)
    
    elif(n==2):
        withdraw=int(input("Enter the amount to withdraw: "))
        customer.withdraw(withdraw)
    
    elif(n==3):
        customer.check_balance()
    
    elif(n==4):
        break
    else:
        print("Invalid input enter again")
        
        