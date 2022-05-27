def fibo_list(n):
    fib_list = [1] * n
    for i in range(2, len(fib_list)):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return 0 if n == 0 else fib_list[-1]

if __name__ == '__main__':
    n = int(input())
    print(fibo_list(n))

