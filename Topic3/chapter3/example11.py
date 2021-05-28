# 피보나치수열 공간 최적화

def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트
    for i in range(1, n):
        current, previous = current + previous, current

    # n번째 피보나치 수를 리턴
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

