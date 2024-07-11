mylist=[19,23,54,13,56,12,56,13]
mylist.sort(reverse=True)
print(mylist)
x=int(input('enter number to search'))
print(x)
pos=0
low=0
flag=1
high=len(mylist)
mid=(low+high)//2
while(low!=high):
    if x==mylist[mid]:
        print('Index Position of element in array:',mylist.index(mylist[mid]))
        flag=0
        break
    elif x>mylist[mid]:
        high=mid
        mid=(high+low)//2        
    else:
        low=mid
        mid=(high+low)//2
if flag==1:
    print('Element not present in list')
    

# the purpose of this code is to find the index position
# of an element in a list that is sorted in the reverse order
# we use binary search to find the position of the element