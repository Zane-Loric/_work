#Same thing reversed 
def Seq(User_input):
    for i in range(User_input,0,-1):
        print(" "*(User_input-i),end="")
        print("*"*(2*i-1), end="")
        print()
User_input = int(input("Enter a number: "))
Seq(User_input)
#Created by Zane-Loric