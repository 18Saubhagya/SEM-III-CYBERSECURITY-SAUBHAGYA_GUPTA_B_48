check_str=input("ENTER THE STRING\n")
list1=[]
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
    list1.append(0) 
for i in range(0,26):
    if list2[i] in check_str.lower():
        list1[i]=1
if 0 in list1:
    print("NOT A PANAGRAM")
else:
    print("PANAGRAM")