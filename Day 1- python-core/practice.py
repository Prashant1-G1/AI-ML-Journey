#number guessing game
import random




is_running=True
count=0
while is_running:
    guess=int(input("enter the number (1-10): "))
    number=random.randint(1,10)
    count+=1
    if guess==number:
        print("You are right")
        print(f"Try={count}")
        is_running=False
    else:
        print("You are wrong")
        print(f"the number was= {number}")
        print(f"Try={count}")
    
    



