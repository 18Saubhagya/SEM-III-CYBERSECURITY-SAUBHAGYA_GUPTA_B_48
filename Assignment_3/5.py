list1=list(map(int,input("ENTER THE NUMBERS\n").split()))
f=0
for i in range(0,len(list1)):
    if list1[i]==3:
        if list1[i+1]==3:
            f=1
            print("true")
            break
if(f!=1):
    print("false")