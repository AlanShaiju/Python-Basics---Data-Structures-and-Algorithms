arr=[]
fibDict={}
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        if(n in list(fibDict.keys())):
            return(fibDict[n])
        else:
            fibDict[n]=fibonacci(n-1)+fibonacci(n-2)
            return(fibDict[n])

# Example usage:
n_terms = 100

print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i))
