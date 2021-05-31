# 최소 동전으로 거슬러 주기

def min_coin_count(value, coin_list):
    min_coin = 0
    coin_list = sorted(coin_list, reverse= True)

    for i in range(len(coin_list)):
        coin = value // coin_list[i]
        min_coin += coin
        value = value - coin*coin_list[i]

    return min_coin



# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))