from random import randint
x = randint(1,10)
i = 0

def prod():
    guess = int(input("Enter your guess :"))
    if guess > x :
        print("enter a smaller value")
    elif guess < x :
        print("enter a larger value")
    else :
        print("correct")
        print("Chances used :", i)
while(1):
    i=i+1
    print(" 1. Guess")
    print("2. Quit")
    choice = int(input("Enter your choice : "))
    if choice == 1 :
        prod()

    elif choice == 2 :
        exit()
    else :
        print("Please enter a valid number ")