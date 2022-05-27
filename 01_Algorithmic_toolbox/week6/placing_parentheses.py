# uses python3

def calc_exp(l:int, op:str, r:int):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    else:
        return l * r


def calc_min_max(i, j, min_table, max_table, ops):
    min_res = float('inf')
    max_res = float('-inf')
    
    for k in range(i, j):
        a = calc_exp(max_table[i][k], ops[k], max_table[k + 1][j])
        b = calc_exp(max_table[i][k], ops[k], min_table[k + 1][j])
        c = calc_exp(min_table[i][k], ops[k], max_table[k + 1][j])
        d = calc_exp(min_table[i][k], ops[k], min_table[k + 1][j])
        min_res = min(min_res, a, b, c, d)
        max_res = max(max_res, a, b, c, d)
        
    return min_res, max_res


def get_max_value(nums, ops):
    n = len(nums)
    min_table = [[0] * n for i in range(n)]
    max_table = [[0] * n for i in range(n)]

    for i in range(n):
        min_table[i][i] = max_table[i][i] = nums[i]

    for size in range(1, n):
        for i in range(0, n - size):
            j = i + size
            min_table[i][j], max_table[i][j] = calc_min_max(i, j, min_table, max_table, ops)
    
    return max_table[0][n - 1]


if __name__ == '__main__':
    
    exp = input()
    nums = []
    ops = []
    for i in range(len(exp)):
        if i % 2 == 0:
            nums.append(int(exp[i]))
        else:
            ops.append(exp[i])

    print(get_max_value(nums, ops))