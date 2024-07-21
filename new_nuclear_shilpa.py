def oppy(targets, dropping):
    l=[]
    for i in targets:
        differences=[]
        for j in dropping:
            differences.append(abs(i-j))
        l.append(min(differences))
    print(max(l))

target=[2,4,5,10,15,17]
drops=[3,7]
oppy(target,drops)