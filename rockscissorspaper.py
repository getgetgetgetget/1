import random

ties=0
wins=0
loses=0
print('ties=0, wins=0, loses=0')
print("Welcome to our digital rock scissors and paper game. In this game, 1 represents rock, 2 represents scissors, and 3 represents paper.")

a=random.randint(1,3)

x = input("Enter your choice : ")
x=int(x)
if(x==a):
    print("It is a tie.")
    print(ties+1)
if(x>a):
    print("You won!")
    print(wins+1)
if(x<a):
    print("You were defeated.")
    print(loses+1)
