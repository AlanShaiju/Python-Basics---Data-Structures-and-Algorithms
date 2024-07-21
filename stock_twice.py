ml=[310,315,275,260,270,290,230,255,250]
max_profit=0
m=ml[0]
buy_index=0
sell_index=0
for i in range(1,len(ml)):
    if ml[i]<m:
        m=ml[i]
        buy_index=i
    if max_profit<(ml[i]-m):
        max_profit=ml[i]-m
        sell_index=i
print(max_profit)
max_profit_2=0
m=None
for i in range(0,len(ml)): 
    if (i<buy_index and i<sell_index) or i>sell_index:
        if m==None:
            m=ml[i]
        if ml[i]<m:
            m=ml[i]
        if max_profit_2<(ml[i]-m):
            max_profit_2=ml[i]-m
print(max_profit_2)
total_profit=max_profit+max_profit_2
print(total_profit)