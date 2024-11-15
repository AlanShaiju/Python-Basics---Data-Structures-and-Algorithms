ml=[4,8,25,69,85,99,101]
mid=len(ml)//2
l=0
h=len(ml)
x=int(input("eNTER NUMBER TO SEARCH"))
while l<=h:
    if ml[mid]==x:
        print('position:',mid)
        break
    if ml[mid]>x:
        h=mid
        mid=(l+h)//2
    elif ml[mid]<x:
        l=mid
        mid=(l+h)//2
