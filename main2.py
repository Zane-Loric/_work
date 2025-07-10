print('''
1- Choose a valid integer between 1 and 100
2- You have 3 chances to guess the number
3- If you guess the number correctly, you win absolutely nothing
4- If you guess the number incorrectly, you lose absolutely nothing
5- Have fun !
''')
# This is a simple number guessing game where the user has to guess a number between 1 and 100.
import random
d = 0
print(f"\t \t \t \t \t \t \t \t \t \t \t \t \t \t \t  High Score: {float(d)}")         
f = "YES"
while f == "YES":
    com = random.randint(1, 100)
    i = 3
    while i > 0:
       # print(com) #Developer option
        b = int(input("Enter Your Guess:   ")) #Valid number input

        #condition if the following input is not a integer

        if (com == b):
            d+= 1
            print("You guessed it right!")
            print(f"The number is {com}, Congratulations!")
            print(f"\t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t  High Score: {float(d)}")         
            break
        elif com > b:
            print("Your guess is too low")
        elif com < b:
            print("Your guess is too high")
    
        i -= 1
        if i > 0:
             print(f"Better Luck Next Time! You have only {i} chances left")
        else:
             print("You have used all your chances")
             print(f"The number was {com}")
             if(b>com):
                print(f"you were {b-com} numbers away from the correct answer!")
             elif(b<com):
                print(f"you guess was {com-b} numbers behind from the correct answer!")   
   
    f = input("Do you want to play again:").upper()
print(f"{d} was Your High Score Congratulation \n")
if(d>=15):
    print("You are a pro player\n")
elif(d==0):
    print("You are unlucky like most of us \n")
else:
    print("That was mild\n")


print('''
Thank You for haveing your time with us
We hope you enjoyed the game
Rate 5 star else gay....
''')