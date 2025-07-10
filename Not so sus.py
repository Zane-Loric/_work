print('''
1- Choose a valid integer between 1 and 100
2- You have 3 chances to guess the number
3- If you guess the number correctly, you win absolutely nothing
4- If you guess the number incorrectly, you lose absolutely nothing
5- Have fun !
''')
import random
com = random.randint(1, 100)
f = "YES"
while f == "YES":
    i = 3
    while i > 0:
        b = int(input("Enter Your Guess:   ")) #Valid number input
    
        #condition if the following input is not a integer

        if (com == b):

            print("You guessed it right!")
            print(f"The number is {com}, Congratulations!")
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
    
    f = input("Do you want to play again? (YES/NO): ").upper()

print('''
Thank You for haveing your time with us
    We hope you enjoyed the game
''')