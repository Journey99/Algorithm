# cache를 이용한 피보나치 수열

def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않은 경우
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))