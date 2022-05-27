# Uses python3

def fib_sum(n):

    fib_list = [0] * 60
    fib_list[1] = 1

    for i in range(2, len(fib_list)):
        fib_list[i] = (fib_list[i - 1] + fib_list[i - 2]) % 10
        if fib_list[i] == 1 and fib_list[i - 1] == 0:
            break

    n_plus_two_last_dig = fib_list[(n + 2) % 60]
    return (n_plus_two_last_dig - 1) if n_plus_two_last_dig > 0 else 9


if __name__ == '__main__':
    n = int(input())
    print(fib_sum(n))   
