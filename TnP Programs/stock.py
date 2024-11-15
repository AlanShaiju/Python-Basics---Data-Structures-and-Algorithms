from statistics import median
ml=[75,36,29,78,20,91,36,45,75,36,95]
length=len(ml)
mean_ml=sum(ml)/length
nml=[]
for i in range(0,len(ml)):
    val=ml[i]-mean_ml
    nml.append(val)
smol=min(nml)
pos=nml.index(smol)
big=max(val for val in nml if val>smol and nml.index(val)>nml.index(smol))
pos2=nml.index(big)
print(ml)
print(nml)
print('best day to buy:',pos)
print('Sell day:',pos2)

#check by seeing elemenmt to element and see which has minimum diff 