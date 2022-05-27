# uses python3

def partition(nums, n):
    summ = sum(nums)
    if summ % 3 != 0 or len(nums) < 3:
        return 0

    point = int(summ / 3 * 2)
    
    value = [[0] * (point + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        if nums[i - 1] > point / 2:
            return 0
        for num in range(1, point + 1):
            ifnotgrab = value[i - 1][num]
            value[i][num] = ifnotgrab
            if nums[i - 1] <= num:
                ifgrab = value[i - 1][num - nums[i - 1]] + nums[i - 1]
                value[i][num] = max(ifnotgrab, ifgrab)

    # print(value[n][point])   
    # print(value[n][int(point / 2)])
    
    return 1 if value[n][point] == (2 * value[n][int(point / 2)]) == point else 0


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(partition(nums, n))