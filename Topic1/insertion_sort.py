"""
삽입 정렬(insertion sort)
 : 각 값이 어떤 인덱스에 들어가야할지 찾는 알고리즘
 ex) 카드 게임을 한다고 할 때, 이미 정렬된 카드를 가지고 있는 상태에서
     딜러가 새로운 카드를 줬을 때, 새로운 카드를 올바른 위치에 삽입한다.

 - 이미 거의 정렬된 리스트를 정렬할 때는 빠른 반면,
   정반대로 정렬된 리스트의 경우 매우 오래 걸린다.
"""

def insertion_sort(some_list):
        for i in range(1, len(some_list)):
            for j in range(i, 0, -1):
                if some_list[j] < some_list[j-1]:
                    some_list[j], some_list[j-1] = some_list[j-1], some_list[j]
                else:
                    break

        return some_list