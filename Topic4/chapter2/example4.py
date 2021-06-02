# 계단 오르기

def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))


"""
피보나치 수열로 생각하면 된다.
예를 들어 n이 6이라고 해보자
그럼 4번째, 5번째 계단을 오르는 방법을 세서 더하면 된다
그렇다면 4번째 계단을 오르는 수는 2,3번째 계단을 오르는 방법을 세면 된다 -> 피보나치!
"""