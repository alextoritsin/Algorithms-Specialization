# Uses python3
import math


def get_min_coints(coins, money):
    min_nums = [0] * (money + 1)
    for m in range(1, money + 1):
        min_nums[m] = math.inf
        for coin in coins:
            if m >= coin:
                min_num = min_nums[m - coin] + 1
                if min_num < min_nums[m]:
                    min_nums[m] = min_num

    return min_nums[money]


if __name__ == '__main__':
    coins = [1, 3, 4]

    money = int(input())

    print(get_min_coints(coins, money))



