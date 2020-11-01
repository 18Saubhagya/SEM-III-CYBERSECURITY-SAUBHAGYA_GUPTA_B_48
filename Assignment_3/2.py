n1=int(input("Enter number 1\n"))
n2=int(input("Enter number 2\n"))
if(n1%2==0 and n2%2==0):
    print(min(n1,n2))
else: print(max(n1,n2))