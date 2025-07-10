k = 5
def sk(k):
    for i in range(1,6):
        print(f"{k}"*i,end="")
        print("")
        k-=1

sk(k)