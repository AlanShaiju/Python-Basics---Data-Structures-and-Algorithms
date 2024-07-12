arr=[1,12,4,11,9,43,98,2,23,65]
b=[0]*len(arr)
print(arr)
def mergesort(arr,low,high):
    mid=(low+high)//2
    if(low<high):
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    h=low
    i=low
    j=mid+1
    while((h<=mid)and(j<=high)):
        if arr[h]<arr[j]:
            b[i]=arr[h]
            h+=1
        else:
            b[i]=arr[j]
            j+=1
        i+=1
    if mid<h:
        for k in range(j,high+1):
            b[i]=arr[k]
            i+=1
    else:
        for k in range(h,mid+1):
            b[i]=arr[k]
            i+=1
    for k in range(low,high+1):
        arr[k]=b[k]
        

mergesort(arr,0,len(arr)-1)   
print(arr)        
            
            