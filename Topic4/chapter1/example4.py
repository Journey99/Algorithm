# 중복되는 숫자 찾기

def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))


# 시간복잡도는 O(n)이 된다.

def find_same_number(some_list):
    # 가능한 모든 조합을 다 돌면서 반복 요소가 있는지 확인하고 있으면 해당 요소를 리턴한다
    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]

# 위와 같이 for문으로 풀면 for문이 두번 반복되기 때문에 시간복잡도는 O(n^2)이 된다.