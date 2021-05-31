# 거듭제곱 빠르게 구하기

def power(x, y):
    total = 1

    # x를 y번 곱해 준다
    for i in range(y):
        total *= x

    return total

# 위와 같이 계산하게 되면 시간 복잡도는 O(y)가 된다

def power(x, y):
    # Base Case
    if y == 0:
        return 1

    # Recursive Case
    return x * power(x, y - 1)

# 이것 또한 시간 복잡도는 O(y)가 된다

def power(x, y):
    if y == 0:
        return 1

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    else:
        return x * power(x, y // 2) * power(x, y // 2)


# 추가적으로 power(2, 2), power(2, 4), power(2, 8)에 대한 호출이 몇 번씩 있기 때문에 이 솔루션도 최소 O(y)

def power(x, y):
    if y == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    subresult = power(x, y // 2)

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# 최적 부분 구조와 중복되는 부분 문제가 있으니, 이 문제는 Dynamic Programming으로 해결하면 된다.
# 다만, 이 경우에는 일반적인 Memoization이나 Tabulation 방법보다 훨씬 간단하게 해결할 수 있습니다.
