import time

hour=int(input("enter current hr:"))
min=int(input("enter current min:"))
sec=int(input("enter current sec:"))

def display():
    print("hour",":","min",":","sec")
    print(hour,':',min,':',sec)
def add():
    global hour
    global min
    global sec
    
    sec+=1
    if sec==60:
        min+=1
        sec=0
    if min==60:
        hour+=1
        min=0
    if hour==24:
        hour=0
print('/n')
while True:
    time.sleep(1)
    add()
    display()