a = int(input("Enter a number pls: "))
def Sa(a):
    for i in range(1,a+1):
        print(" "*(a-i), end="")
        print("*"*i,end="")
        print("")

Sa(a)