#Python program to generte a simple alphabet pyramid via user input
def Seq(User_Input):
    for i in range(1,User_Input+1):
        print(" "*(User_Input-i), end ="")       #Same Logic as simple star pyramid
        print(f"{chr(64+i)}"*(2*i-1), end = "")   # chr 64 == A +1 == B ----
        print(" ")           
User_Input = int(input("Enter a number: "))
Seq(User_Input)