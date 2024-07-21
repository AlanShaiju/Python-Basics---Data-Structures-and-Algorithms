target=[2,4,5,10,15,17]
drops=[3,7]
devastation=[max(abs(max(drops)-min(target)),abs(max(target)-min(drops)))]*len(target)
for i in drops:
    for j in range(0,len(target)):
        if devastation[j]> abs(i-target[j]):
            devastation[j]=abs(i-target[j])
print(max(devastation))
# O(nlog(n)) for processing
#  O(1) for storage
