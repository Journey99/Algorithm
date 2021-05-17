""""
이진 탐색 알고리즘(binary search algorithm)
 :정렬된 리스트를 전제로 한다. (정렬 안된 리스트는 이진 탐색 알고리즘 적용 불가)
  반씩 제외시키면서 찾는 방법
"""

#이진탐색알고리즘
def binary_search(element, some_list):

    first_index = 0
    last_index = len(some_list) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2

        if element == some_list[mid_index]:
            return mid_index
        elif element < some_list[mid_index]:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))