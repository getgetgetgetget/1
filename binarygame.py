import random

print("In this game, you are to guess a number between 1 to 2000. Try for your best record!")
a=random.randint(1,2000)

attempts=0
while(attempts<2001):
    x = input("Take a while guess : ")
    x = int(x)
    attempts+=1
    if(x>a):
        print("number should be smaller. The number right is the number of your attempts:" + str(attempts))
    if(x<a):
        print("number should be larger. The number right is the number of your attempts:" + str(attempts))
    if(x==a):
        print("You are correct! The number right is the number of your attempts:" + str(attempts))
        attempts+=2002
