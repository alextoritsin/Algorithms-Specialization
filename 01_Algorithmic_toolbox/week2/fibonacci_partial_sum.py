# Uses python3

def fib_partial_sum(m, n):

    fib_list = [0] * 60
    fib_list[1] = 1

    for i in range(2, len(fib_list)):
        fib_list[i] = (fib_list[i - 1] + fib_list[i - 2]) % 10
    
    if n == m:
        return fib_list[n % 60]
    else:
        n_plus_two_last_dig = fib_list[(n + 2) % 60]
        sum_n = (n_plus_two_last_dig - 1) if n_plus_two_last_dig > 0 else 9

        if m == 0:
            return sum_n

        sum_before_m = fib_list[(m + 1) % 60]
        sum_m = (sum_before_m - 1) if sum_before_m > 0 else 9

        result = sum_n - sum_m
        return result if sum_n >= sum_m else result + 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fib_partial_sum(m, n))