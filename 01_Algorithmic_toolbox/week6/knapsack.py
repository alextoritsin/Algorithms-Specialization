# uses python3

def knapsack(weights, W, n):
    value = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            ifnotgrab = value[i - 1][w]
            value[i][w] = ifnotgrab
            if weights[i - 1] <= w:
                ifgrab = value[i - 1][w - weights[i - 1]] + weights[i - 1]
                value[i][w] = max(ifnotgrab, ifgrab)

        
    
    return value[n][W]


if __name__ == '__main__':
    W, n = [int(i) for i in input().split()]
    weights = [int(i) for i in input().split()]

    print(knapsack(weights, W, n))