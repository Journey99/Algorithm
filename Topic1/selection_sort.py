"""
정럴(Sorting) : 리스트의 원소들을 특정 순서로 정리하는 것
  - 오름차순, 내림차순, 알파벳순 .....
  - 내장함수인 sorted(list) / 리스트의 list.sort() method가 있다.

선택 정렬(selection sort)
 :각 인덱스에 들어갈 값들을 찾아서 정렬하는 알고리즘
 - 가장작은값은 0번 인덱스, 2번째 작은값은 1번 인덱스...

"""


# 원소를 1:1 교체해주는 swap함수
def swap(some_list, i, j):
    some_list[i], some_list[j] = some_list[j], some_list[i]

def selection_sort(some_list):
    for i in range(len(some_list)):
        min_index = i

        for j in range(min_index + 1, len(some_list)):
            if some_list[min_index] > some_list[j]:
                swap(some_list, min_index, j)

    return some_list