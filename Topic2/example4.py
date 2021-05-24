# 리스트 뒤집기

def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    return some_list[-1:] + flip(some_list[:-1])

# some_list[-1: ] == 마지막에 있는 인자 하나
# some_list[ :-1] == 마지막걸 뺀 인자 모두


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
