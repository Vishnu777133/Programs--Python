import random
print("1=rock")
print("2=paper")
print("3=scisser")
print()
print()

x=random.randint(1,3)
num=int(input("enter 1=rock,2=paper or 3=scissor:"))
print("computer:",x)
print("your no:",num)
print()
print()

if num==x:
        print("result:tie")
elif num==1 and x==2:
    print("result:you loss")
elif x==1 and num==2:
    print("result:you win")
elif num==2 and x==3:
    print("result:you loss")
elif num==3 and x==2:
    print("result:you win")    
elif num==1 and x==3:
    print("result:you win")
elif x==1 and num==3:
    print("you loss")    
else:
    print("typing error")

       