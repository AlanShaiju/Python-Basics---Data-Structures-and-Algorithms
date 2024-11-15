import math
x=int(input('Enter the number:'))
y=math.floor(math.log10(x))
temp=x
b=0
if y/2!=0:
    fh=temp//(10**((y+1)//2))
    fh=fh//10
    print(fh)
    for i in range(0,(y+1)//2):
        b=b*10+temp%10
        temp=temp//10
        print(temp)
        print(b)
    if fh==b:
        print('pallindrome')
    else:
        print('not pallindrome')
else:
    fh=temp//(10**((y+1)//2))
    for i in range(0,(y+1)//2): 
        b=b*10+temp%10
        temp=temp//10
    if fh==b:
        print('pallindrome')
    else:
        print('not pallindrome')      
    
    
    
    