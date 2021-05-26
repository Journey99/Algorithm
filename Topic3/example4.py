# 1부터 n까지의 합을 분할정복으로

# 내가 풀은 것
def consecutive_sum(start, end):
    # 코드를 작성하세요
    if start == end:
        return start
    return end + consecutive_sum(start, end -1)
# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

# 해답
def consecutive_sum(start, end):
    # base case
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))