"""
< 재귀함수 - recursive function >
: 재귀 함수란 어떤 함수에서 자신을 다시 호출하여 작업을 수행하는 방식의 함수를 의미한다.
  반복문을 사용하는 코드는 항상 재귀 함수를 통해 구현하느 것이 가능하며 그 반대도 가능하다.
  종료 조건이 꼭 포함되어야 한다.


ex)
-   def countdown(n):
        if n > 0:
            print(n)
            countdown(n-1)

    countdown(4)

- 팩토리얼(factorial)
    def factorial(n):
        if n == 0:
            return 1
        return factorial(n-1) * n

    print(factorial(4))






"""