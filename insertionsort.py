mylist=[1,12,4,11,9,43,98,2,23,65]
print(mylist)
for i in range(1,len(mylist)):
    for j in range(i,0,-1):
        if mylist[j]<mylist[j-1]:
            temp=mylist[j]
            mylist[j]=mylist[j-1]
            mylist[j-1]=temp
print(mylist)     