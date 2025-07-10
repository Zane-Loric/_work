a = int(input("Enter a value: "))
def fs(a):
    for i in range(1,a+1):
        print(" "*(a-i),end="")
        print("*"*(2*i-1),end="")
        print("")

fs(a)