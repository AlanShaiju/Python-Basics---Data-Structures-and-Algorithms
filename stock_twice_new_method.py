ml=[310,337,275,260,270,290,230,255,250]
forward=[]
backward=[]
max_profit=0
m=ml[0]
for i in range(0,len(ml)):
    if ml[i]<m:
        m=ml[i]
    if max_profit<(ml[i]-m):
        max_profit=ml[i]-m
    forward.append(max_profit)
print(forward)
max_profit=0
m=ml[len(ml)-1]
for i in range(len(ml)-1,-1,-1):
    if ml[i]>m:
        m=ml[i]
    if max_profit<(m-ml[i]):
        max_profit=(m-ml[i])
    backward.append(max_profit)
backward.reverse()
print(backward)
maximum=0
for i in range(0,len(ml)-1):
    if maximum<forward[i]+backward[i+1]:
        maximum=forward[i]+backward[i+1]
print(maximum)