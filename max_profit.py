ml=[215, 265, 250, 200, 240, 260, 230]
max_profit=0
m=ml[0]
for i in range(1,len(ml)):
    if ml[i]<m:
        m=ml[i]
    if max_profit<(ml[i]-m):
        max_profit=ml[i]-m
print(max_profit)