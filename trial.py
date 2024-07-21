q=[[1,5,3],[4,8,7],[6,9,1]]
n=10
l=[0]*(n+1)
m=0
s=0
for a,b,c in q:
    l[a]=l[a]+c
    l[b+1]=l[b+1]-c
for i in range(0,len(l)):
    s=s+l[i]
    if m<s:
        m=s
print(m)
