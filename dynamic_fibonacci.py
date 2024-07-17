# def fib(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 0
#     return fib(n-1)+fib(n-2)
# print(fib(10000))
 
# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1
 
def fibonacci_optimized(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Example usage:
n = 1000
print(f"Fibonacci number at position {n} is {fibonacci_optimized(n)}")