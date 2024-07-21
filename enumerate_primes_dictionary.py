n=100000000
is_prime={}
for i in range(2,n+1):
    is_prime[i]=True
for i in is_prime.keys():
    if is_prime[i]:
        for j in range(2,n,i):
            is_prime[j]=False
print(is_prime)