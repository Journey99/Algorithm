# Divide and Conquer 방식으로 최대수익 구간구하기

def sublist_max(profits, start, end):
    # 범위에 하나의 항목밖에 없으면(base case)
    if start == end:
        return profits[start]

    mid = (start + end) // 2
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid+1, end)
    max_cross = max_crossing_sum(profits, start, end)

    return max(max_left, max_cross, max_right)


def max_crossing_sum(profit, start, end):
    mid = (start + end) // 2

    '''
    왼쪽에서 가장 큰 수익 계산
    '''
    left_sum = 0
    left_max = profit[mid]

    for i in range(mid, start-1, -1):
        left_sum += profit[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서 가장 큰 수익 계산
    '''
    right_sum = 0
    right_max = profit[mid + 1]

    for i in range(mid + 1, end+1):
        right_sum += profit[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max





# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))