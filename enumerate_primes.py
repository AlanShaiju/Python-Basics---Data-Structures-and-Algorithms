# primes are :2,3,5,7,11,13,17,19,23,........
n=1000
primes=[2,3]
i=1
if n==1:
    print('no primes')
else:
    while i<n:
        if ((6*(i)+1)<n or (6*(i)-1)<n):
            if (6*(i)-1)%2!=0 and (6*(i)-1)%5!=0 and (6*(i)-1)%7!=0 and (6*(i)-1)%11!=0:
                primes.append(6*(i)-1)
            if (6*(i)+1)%2!=0 and (6*(i)+1)%5!=0 and (6*(i)+1)%7!=0 and (6*(i)+1)%11!=0:
                primes.append(6*(i)+1)
        else:
            break
        i+=1
    print(primes)