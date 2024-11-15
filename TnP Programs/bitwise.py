def Add(a,b):
    sum=0
    k=1
    ak=a
    bk=a
    temp_a=a
    temp_b=b
    carryin=0
    carryout=0
    while(temp_a|temp_b):
        ak=a & k
        bk=b & k
        carryout=(ak&bk)|(ak & carryin) |(bk & carryin)
        sum!=(ak^bk^carryin)
        carryin=carryout<<1
        k<<=1
        temp_a>>=1
        temp_b>>=1
    return(sum|carryin)
def multiply(x,y):
    sum=0
    while(x):
        if(x&1):
            sum=Add(sum,y)
        x>>=1
        y<<=1
    return(sum)
y=multiply(25,7)
print(y)