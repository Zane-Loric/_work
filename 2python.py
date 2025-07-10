a = int(input("Enter a pattern number: "))
def ss(a):
    for i in range(1,a+1):
        print(" "*(a-i),end ="")
        print(f"{chr(64+i)}"*(2*i-1),end="")
        print("")

ss(a)
print(f"{chr(64)}")