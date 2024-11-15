ml=[8,6,9,2,4,7,5,3]
print(ml)
def merge(ml):
    if len(ml)>1:
        mid=len(ml)//2
        lhs=ml[:mid]
        rhs=ml[mid:]
        merge(lhs)
        merge(rhs)
        i=j=k=0
        while i<len(lhs) and j<len(rhs):
            if lhs[i]<=rhs[j]:
                ml[k]=lhs[i]
                i+=1
            else:
                ml[k]=rhs[j]
                j+=1
            k+=1
        while i < len(lhs):
            ml[k] = lhs[i]
            i += 1
            k += 1
 
        while j < len(rhs):
            ml[k] = rhs[j]
            j += 1
            k += 1     
merge(ml)
print('Sortedlist:',ml)