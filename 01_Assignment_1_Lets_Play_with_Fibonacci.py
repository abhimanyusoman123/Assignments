

n=int(input("Enter the Range Number:"))
n1=0
n2=1
for i in range(0,n):
    if (i<=1):
        t=i
        print(t,end=",")
    else:
        t=n1+n2
        n1=n2
        n2=t
        print(t,end=",")

