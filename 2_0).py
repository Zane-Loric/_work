#python program to generate a pyramid structure asking input from user
'''
        *
       ***
      *****
     *******
'''
def Seq(User_input):
    for i in range(1,User_input+1):
        print(" "*(User_input-i),end="")
        print("*"*(2*i-1), end="")
        print()
User_input = int(input("Enter a number: "))
Seq(User_input)
#By zane-Loric