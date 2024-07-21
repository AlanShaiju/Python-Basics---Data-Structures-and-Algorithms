s='UUDDDDUDUU'
mylist=list(s)
s=0
valleys=0
for i in range(0,len(mylist)):
    if mylist[i] == 'U':
        s+=1
    if mylist[i]=='D':
        s-=1
    if s==0:
        if mylist[i]=='U':
            valleys+=1
print(valleys)