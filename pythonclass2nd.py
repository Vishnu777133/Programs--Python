# create a bank software using class:-
class Bank():
  def __init__(self):
    self.balance=1000
    
  def get_balance(self):
    return self.balance
    
  def withdraw(self,amount):
    self.balance=self.balance-amount
    return amount
    
my_bank=Bank()
my_bank.withdraw(500)
balance=my_bank.get_balance()
print(balance)
my_bank.withdraw(50)
balance=my_bank.get_balance()
print(balance)
print()
print("second class:-")

# if bank make new rule that you can withdraw minRs100,
#if you want you withdraw less than Rs100 you can't.
#for this you can use if-else statment:-
class Bank:
  def __init__(self):
    self.balance=1000
    self.minimum=100
    
  def get_balance(self):
    return self.balance
    
  def withdraw(self,amount):
    if amount<self.minimum:
      print("you can't withdraw money")
    elif amount>self.balance:
      print("no money 💰!")
    else:
      self.balance=self.balance-amount
      return amount
    
my_bank=Bank()
my_bank.withdraw(500)
balance=my_bank.get_balance()
print(balance)
my_bank.withdraw(50)
balance=my_bank.get_balance()
print(balance)
  
  
  

