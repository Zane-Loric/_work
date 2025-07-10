a = int(input("Enter a number\t"))
b = int(input("ENter a number\t"))
c = int(input("Enter a number\t"))
d = int(input("ENter a number\t"))
if(a>b and a>c and a>d):
    print(f"{a} is the greatest number")
elif(b>a and b>c and b>d):
    print(f"{b} is the greatest number")        #Multiple conditional statement
elif(c>a and c>b and c>d):
    print(f"{c} is the greatets number")
else:
    print(f"{d} is the greatest number")
print("THe end ")

