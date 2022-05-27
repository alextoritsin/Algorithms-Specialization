# Uses python3

def fibo_huge_mod(n, m):

    fib_list = [0] * m * 6
    fib_list[1] = 1

    for i in range(2, len(fib_list)):
        fib_list[i] = (fib_list[i - 1] + fib_list[i - 2]) % m
        if fib_list[i] == 1 and fib_list[i - 1] == 0:
            break

    pi_m = i - 1
    return fib_list[n % pi_m] % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibo_huge_mod(n, m))