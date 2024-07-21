levels=[2,0,4,2,1,1,2,1]
water=0
stack=[]
top=None
m=None
#going front
for i in levels:
    if top==None:
        top=i
        m=i
        stack.append(i)
    if i >m:
        while stack:
            water+=(m-stack.pop())
        stack.append(i)
        top=i
        m=i
    else:
        stack.append(i)
        top=i
    print(stack)
    print(water)
while stack:
    x=stack.pop()
    