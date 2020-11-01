list1=list(map(int,input("ENTER THE ELEMENTS\n").split()))
check=[0,0,7]
c=0
for j in range(0,len(list1)):
    if(check[c]==list1[j]):
        c+=1
    if(c==3):
        break
if(c==3):
    print("true")
else:
    print("false")