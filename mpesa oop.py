#define user class
class User:
    def __init__(self,user_id,name,phone):
        self.user_id=user_id    #initialize user id
        self.name=name          #initialize user name
        self.phone=phone        #Initialize phone
        self.account=Account(self)  #creating user account
    def __repr__(self):
        return f"User({self.user_id},{self.name}, {self.phone})"  #Represantation of the user object
# define account class
class Account:
    def __init__(self,user):
        self.user=user
        self.balance=0.0
    def deposit(self,amount):
        if amount >0:     #check if the deposit is more than 0
           self.balance+=amount
           print(f"{amount} deposited.New balance:{self.balance}")
        else:
             print("Deposited Amount must be positive")

    def withdraw(self,amount):
        if 0 <amount <=self.balance:  #check if the withdrawal amount is valid
          self.balance-=amount
          print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
          print("Insufficient funds or Invalid amount")

    def __repr__(self):
        return f"Account( User: {self.user.name}, Balance:{self.balance}"  #Represantation of account object
 #define the transaction class
class Transaction:
    def __init__(self,account,amount,transaction_type):
        self.account=account
        self.amount=amount
        self.transaction_type=transaction_type
    def process(self):
        if self.transaction_type== 'deposit':
           self.account.deposit(self.amount)
        elif self.transaction_type =='withdraw':
             self.account.withdraw(self.amount)
        else:
             print("Invalid transaction type")
    def __repr__(self):
        return f"Transaction(Account: {self.account.user.name},Amount:{self.amount},Type{self.transaction_type}"

# Example usage   // object
user1=User(user_id=1,name="Aisha",phone=712317428)
print(user1)
user2=User(user_id=2,name="Hassan",phone=712445455)
print(user2)

# deposit amount
user1.account.deposit(1000)

user1.account.withdraw(5000)

transaction1=Transaction(user1.account,amount=200,transaction_type='deposit')
transaction1.process()

transaction2=Transaction(user1.account,amount=100,transaction_type='withdraw')
transaction2.process()

print(user1.account)

