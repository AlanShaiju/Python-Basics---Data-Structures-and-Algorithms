levels=[2,0,4,2,1,1,2,1]
m=0
l=[]
r=[]
for i in range(0,len(levels)):
    if levels[i]>m:
        l.append(levels[i])
        m=levels[i]
    else:
        l.append(m)
# print(l)
m=0
for i in range(len(levels)-1,-1,-1):
    if levels[i]>m:
        r.append(levels[i])
        m=levels[i]
    else:
        r.append(m)
r.reverse()
# print(r)
new_levels=[]
for i in range(0,len(levels)):
    new_levels.append(min(l[i],r[i]))
print(new_levels)
water=0
for i in range(0,len(levels)):
    water+=new_levels[i]-levels[i]
print(water)