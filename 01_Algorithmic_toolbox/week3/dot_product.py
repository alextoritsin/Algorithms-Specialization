# Uses python3

def max_profit(values, clicks, n):
    profit = 0
    values = sorted(values, reverse=True)
    clicks = sorted(clicks, reverse=True)
    for i in range(n):
        profit += values[i] * clicks[i]

    
    return profit

if __name__ == '__main__':
    n = int(input())
    click_values = list(map(int, input().split()))
    clicks_count = list(map(int, input().split()))
    print(max_profit(click_values, clicks_count, n))