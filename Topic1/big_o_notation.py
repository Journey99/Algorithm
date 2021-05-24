"""
<빅오 표기법 - big-O notation>
:알고리즘의 효율성을 표기해주는 표기법이다.
 알고리즘의 시간 복잡도와 공간 복잡도를 나타내는데 주로 사용 된다.

ex)
- 선형탐색
    def linear_search(element, some_list):
        i = 0                                   -> O(1)
        n = len(some_list)                      -> O(1)

        while i < n:                            -> O(n)
            if some_list[i] == element:
                return i
            i += 1

        return -1                               -> O(1)

                                            => O(n)

- 이진탐색
    def binary_search(element, some_list):
        start_index = 0                             -> O(1)
        end_index = len(some_list) - 1              -> O(1)

        while star_index <= end_index:              -> O(logn)
            midpoint = (start_index + end_index) // 2
            if some_list[midpoint] == element:
                return midpoint
            elif element < some_list[midpoint]:
                end_index = midpoint - 1
            else:
                start_index = midpoint + 1

        return None                                 -> O(1)

                                                => O(logn)

- sorted 함수 또는 sort 메소드  => O(nlgn)

[주요 시간 복잡도]
- O(1)
  : 반복문이 없으면 대체로 O(1)

- O(n)
 : 반목문이 있고, 반복되는 횟수가 인풋의 크기와 비례하면 일반적으로.

- O(n^2)
 : 반목문 안에 반복문이 있는 경우

- O(log n)
 : 보통 while 문이 있을 때

- O(nlogn)
 : while 문이랑 for 문이 중첩되어 있는 경우


""