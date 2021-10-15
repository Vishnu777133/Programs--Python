print("--first class result:-")
#1 simple calculator using class:
class Calculator:
  brand="my calc"
  
  a=int(input("enter first no:"))
  b=int(input("enter second no:"))
  choose=input("choose any one:+,_,*,/=")
  
  if choose=="+":
    c=a+b
    print(c)
  elif choose=="-":
    c=a-b
    print(c)
  elif choose=="*":
    c=a*b
    print(c)
  elif choose=="/":
    c=a/b
    print(c)
  else:
    print("choose correct option")

my_cal=Calculator()
print(my_cal.brand)

print()
print("--secound class result:-")


#2 using method in class:
class Calculator:
  def calculate(self,a,b):
    return a+b
my_calc=Calculator()
result=my_calc.calculate(4,6)
print(result)
print()
print("--third class result:-")


#3 create a shopping class:
class Shopping:
  cart=[]
  def add_to_cart(self,items):
    self.cart.append(items)
    
coustomer1=Shopping()
coustomer1.add_to_cart("T-shirt")
print(coustomer1.cart)

coustomer2=Shopping()
coustomer2.add_to_cart("Shoes")
print(coustomer2.cart)

print() 
print("--third second class result:-")

##3 If you want to print cart items in diff cart then use __init__:-
class Shopping:
  def __init__(self):
    self.cart=[]
  def add_to_cart(self,items):
    self.cart.append(items)
coustomer1=Shopping()
coustomer1.add_to_cart("T-shirt")
print(coustomer1.cart)

coustomer2=Shopping()
coustomer2.add_to_cart("Shoes")
print(coustomer2.cart)

  



    


  
    


  
  