# 숫자 합
# :n번째 삼각수는 자연수 1부터 n까지의 합

def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)

for i in range(1, 11):
    print(triangle_number(i))