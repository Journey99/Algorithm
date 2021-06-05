# 리스트의 항목 합 탐색

def sum_in_list(search_sum, sorted_list):

    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))


# 이렇게 풀면 시간복잡도가 O(n**2)



# 리스트가 정렬되어 있는걸 이용한다
# 시간복잡도가 O(n)

def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum:  # 합이 찾으려는 숫자일 때
            return True

        if candidate_sum < search_sum:  # 합이 찾으려는 숫자보다 작을 때
            low += 1

        else:  # 합이 찾으려는 숫자보다 클 때
            high -= 1

    # 찾는 조합이 없기 때문에 False 리턴
    return False


# 테스트
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))