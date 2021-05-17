"""
선형 탐색 알고리즘(linear search algorithm)
 : 순서대로 처음부터 끝까지 하나하나씩 찾는 방법
  * 정렬이 안된 리스트에도 적용 가능
"""

# 선형탐색알고리즘
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None

# 테스트
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))