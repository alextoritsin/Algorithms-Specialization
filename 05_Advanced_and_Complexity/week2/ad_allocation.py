# python3
from sys import stdin


def find_pivot_row(A, b, i, n):
    min_elem = float('inf')
    for j in range(n):
        if b[j] >= 0 and b / A[j][i] < min_elem:
            min_elem = b / A[j][i]
            row = j
    
    return row


def find_pivot_column(c):
    min_elem, index = 0, 0
    for i in range(len(c)):
        if c[i] < min_elem:
            min_elem = c[i]
            index = i
    
    return index


def allocate_ads(n, m, A, b, c):
    
    while True:
        column = find_pivot_column(A[-1])
        if not column:
            break
        else:
            row = find_pivot_row(A, b, column, n)
            div = A[row][column]
            # relax matrix row
            if div != 1:
                for i in range(n + m):
                    A[row][i] /= div
            b[row] /= div

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row:
                    div = -A[j][column] / A[row][column]
                    for k in range(n + m):
                        A[j][k] += A[row][k] * div
                    b[j] += b[row] * div
            




    

    return [0, [0] * m]
    
    




if __name__ == '__main__':
    
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]
        aux = [0] * m
        aux[i] = 1
        A[i] += aux
    b = list(map(int, stdin.readline().split())) + [0]
    c = list(map(lambda x: int(x) * (-1), stdin.readline().split())) + [0] * m
    A.append(c)

    anst, ansx = allocate_ads(n, m, A, b, c)

    if anst == -1:
        print("No solution")
    if anst == 0:  
        print("Bounded solution")
        print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
    if anst == 1:
        print("Infinity")
    
