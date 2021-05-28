"""
< 동적 계획법(dp) - Dynamic Programming >
: 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법
  한 번 계산한 결과를 여러번 사용!


- 만족시켜야 하는 두 가지 속성
   *부분 반복 문제 (Overlapping Subproblem)
   *최적 부분 구조
      :부분 문제의 최적의 답을 이용해서 기존 문제를 풀 수 있다


- 구현 방법
    1) Memoization
        : 이전의 계산한 값을 메모리에 저장하여 동일한 계산의 반복 수행을 제거
          #이때 저장해 두는 메모리(배열)을 캐시(cache)라고 한다
          # Top-down Approach 하향식 접근
          # 재귀 호출
          # 위에서 부터 내려오기 때문에 필요한 값만 계산할 수 있다
          # 스택이 많이 쌓이면 과부화

        ex) example9

    2) Tabulation
       : Table 방식으로 정리
         # Bottom-up Approach 상향식 접근
         # 반목문 사용
         # n번째 값을 갖기 위해 처음부터 다 계산해야 한다

       ex) example10

"""