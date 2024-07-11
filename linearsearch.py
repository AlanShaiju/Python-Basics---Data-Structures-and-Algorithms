mylist=[12,34,56,2,563,345,65,78,90,24,26,964]
x=int(input('Enter number to search:'))
flag=0
i=0
while( i!=len(mylist)):
    if x==mylist[i]:
        print('Index Position of element:',i)
        flag=1
    i+=1
if(flag==0):
    print('Element not in array')
    
# this program is used to search elements in an array 
# in a linear fashion which means that elements are accessed one
# at a time leading to a time complexity of O(n)
