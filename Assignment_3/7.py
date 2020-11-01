list1=list(map(int,input("ENTER THE ELEMENTS\n").split()))
sum1=sum(list1)
d=0
for i in range(0,len(list1)):
    if(list1[i]==6):
        j=i
        while(list1[j]!=9 and j<len(list1)):
            d+=list1[j]
            j+=1
        sum1-=(d+9)
        i=j
print(sum1)