list1=list(map(int,input("ENTER THREE NUMBERS BEWTWEEN 1 AND 11\n").split()))
flag=0
for i in range(0,3):
    if(list1[i]>11 or list1[i]<1):
        flag=1
        print("error")
        break
if(flag!=1):
    s=sum(list1)
    if s>21:
        if 11 in list1:
            s-=10
            if(s>21):
                print("BUST")
            else:
                print(s)
        else:
            print("BUST")
    else:
        print(s)