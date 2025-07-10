a = int(input("Enter The value: "))
def sk(a):
    for i in range(1,a+1):
       if(i==1 or i==a):
            print("*"*a,end="")
            print("")
       else:
            print("*",end="")
            print(" "*(a-2),end="")
            print("*")

sk(a)
