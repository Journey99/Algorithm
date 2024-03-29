"""
< 분할 정복 - divide and conquer >
: 분할 정복 알고리즘은 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서
  다시 합병하여 문제의 답을 얻는 알고리즘이다.

- 알고리즘 설계 요령
   1) Divide : 문제가 분할이 가능한 경우, 2개 이상의 문제로 나눈다.
   2) Conquer(정복하다) : 나누어진 문제가 여전히 분할이 가능하면 , 또 다시 divide를
                        수행한다. 그렇지 않으면 문제를 푼다
   3) Combine : Conquer한 문제들을 통합하여 원래 문제의 답을 얻는다.

   * divide를 제대로 하는 것이 가장 중요하다.
   * 재귀 알고리즘이 많이 사용된다.

"""