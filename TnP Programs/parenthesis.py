x=input('Enter the string:')
ml=list(x)
flag=0
print(ml)
print(len(ml))
for i in range (0,len(ml)):
    if ml[i]=='{':
        flag+=1
    if ml[i]=='}':
        flag-=1
    if flag<0:
        print('not match')
        break
if flag==0:
    print('match')
else:
    print('not Match')