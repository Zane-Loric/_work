a = int(input("Enter a number: "))
def d(a):
    for i in range(1,a+1):
        print(" "*(a-i),end="")
        print("*"*(2*i-1), end="")
        print("")

d(a)
