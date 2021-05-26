"""
분할정복의 응용
< 퀵 정렬 - quick sort >
: 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬에 속한다.
  분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑한다.

- 알고리즘
  1) 리스트 안에 있는 한 요소를 선택한다. 이를 피벗(pivot)이라고 한다
  2) 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고
     피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨진다.
  3) 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
     -> 분할된 부분 리스트에 대하여 순환 호출 이용하여 정렬
  4) 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.

* 퀵 정렬의 코드는 example7,8




"""