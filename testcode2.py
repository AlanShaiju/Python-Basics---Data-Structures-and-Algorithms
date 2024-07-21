n=10
mylist=[0]*n
q=[[1,5,3],[4,8,7],[6,9,1]]
for i in q:
    for j in range(i[0],i[1]+1):
        mylist[j]=mylist[j]+i[2]
m=max(mylist)
print(m)    


# 0 0 0 0 0 0 0 0 0 0