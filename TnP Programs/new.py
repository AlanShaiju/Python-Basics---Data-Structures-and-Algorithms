#given an array of +ve numbers representing heights of stone towers , find the max water stored in total array
size=[3,0,2,0,4,0,1]
water=0
maximum=max(size)
pos=size.index(maximum)
l1=[]
l2=[]
for i in range (0,len(size)):
    if i< pos :
        l1.append(size[i])
    if i>pos:
        l2.append(size[i])
water=0
for i in range(0,len(l1)):
    water=water+max(l1)
    water=water-l1[i]
for i in range(0,len(l2)):
    water=water+max(l2)
    water-water-l2[i]
print(water)
# pos=0
# for i in range (1,len(size)):
#     print(max,min)
#     print(water)
#     if size[i]>max:
#         water=water+max*(i-pos-1)
#         print('max',water)
#         pos=i
#         max=size[i]
#     # else:
#     #     water=water-size[i]
#     if size[i]<min and size[i]!=0:
#         water=water-size[i]
#         print('min',water,size[i])
#         min=size[i]