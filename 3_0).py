def seq(a):
    for i in range(1,a+1):
        print("*"*(a-i),end="") #Number of star in a single row
        print(" ")

a = int(input("Enter the number of rows: "))
seq(a)
#By Zane Loric
