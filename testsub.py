a = int(input('er Your age of consent: '))
if(a>18):
    print("Valid")
elif(a==0):
    print("Invalid")
elif(a<0):
    print("Invalid")
else:                                   #Conditional Statement
    print("Underage")

print("\t Thank You \t")