# Uses python3

def fib_sum_of_squares(n):

    fib_list = [0] * 60
    fib_list[1] = 1

    for i in range(2, len(fib_list)):
        fib_list[i] = (fib_list[i - 1] + fib_list[i - 2]) % 10
    

    sum_of_squares = fib_list[n % 60] * fib_list[(n + 1) % 60]

    return sum_of_squares % 10

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_of_squares(n))