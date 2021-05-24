# 피보나치 수열

def fib(n):
    if n == 1 or n == 2:        # n < 3
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 11):
    print(fib(i))