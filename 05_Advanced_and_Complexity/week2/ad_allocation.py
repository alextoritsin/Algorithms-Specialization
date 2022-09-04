# python3
from sys import stdin


def find_pivot_row(A, rhs, col, n):
    min_elem = float('inf')
    row = -1
    for j in range(n):
        if A[j][col] > 0:
            res = rhs[j] / A[j][col]
            if res < min_elem:
                min_elem = res
                row = j
    
    return row


def find_pivot_column(obj_func, length):
    min_elem, index = 0, length
    for i in range(length):
        if obj_func[i] < min_elem:
            min_elem = obj_func[i]
            index = i
    
    return index


def resolve_tableau(A, rhs, obj_func, exclude):
    while True:
        column = find_pivot_column(A[-1])
        if column == float('inf'):
            return A, rhs

    
    pass



def allocate_ads(n, m, A:list, rhs, z, w, artif_set):
    BV_in_row = [float('inf')] * n
    BV_in_col = [float('inf')] * m
    if w:
        # go to phase One
        A.append(w)
        ln = len(w)
        column = find_pivot_column(A[-1], ln)
        while column != ln:
            row = find_pivot_row(A, rhs, column, n)
            if row == -1:
                return 1, []
            # relax tableau row
            div = A[row][column]
            if div != 1:
                for i in range(n + m):
                    A[row][i] /= div
                rhs[row] /= div

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row and A[j][column]: 
                    div = -A[j][column] / A[row][column]
                    for k in range(ln):
                        A[j][k] += A[row][k] * div
                    rhs[j] += rhs[row] * div

            # rearrange relation btw row and column of bv 
            if column < m:
                if BV_in_row[row] != float('inf'):
                    BV_in_col[BV_in_row[row]] = float('inf')

                BV_in_col[column] = row
            BV_in_row[row] = column

            
            column = find_pivot_column(A[-1], ln)


        # check for infeasibility
        # if one or more artificial values in basic values
        # than we have infeasible solution
        if rhs[-1] < 0:
            return -1, []

        # prepare tableau for phase Two
        A[-1] = z + [0] * (ln - m)
        ln = len(w) - len(artif_set)
        # check variables in z column to be BV and make all other values 0
        for i, row in enumerate(BV_in_col):
            if row != float('inf') and A[-1][i] != 0:
                scale = A[-1][i] * (-1)
                for k in range(ln):
                    A[-1][k] += A[row][k] * scale
                rhs[-1] += rhs[row] * scale

        # BV = [float('inf')] * m
        """Start Phase II"""
        column = find_pivot_column(A[-1], ln)
        while column != ln:
            row = find_pivot_row(A, rhs, column, n)
            if row == -1:
                return 1, []
            
            div = A[row][column]
            # relax tableau row
            if div != 1:
                for i in range(n + m):
                    A[row][i] /= div
                rhs[row] /= div

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row and A[j][column]: 
                    div = -A[j][column] / A[row][column]
                    for k in range(ln):
                        A[j][k] += A[row][k] * div
                    rhs[j] += rhs[row] * div
            if column < m:
                if BV_in_row[row] != float('inf'):
                    BV_in_col[BV_in_row[row]] = float('inf')

                BV_in_col[column] = row
            BV_in_row[row] = column
            
            column = find_pivot_column(A[-1], ln)

        # break out of the loop, optimal solution found
        return 0, [0 if row == float('inf') else rhs[row] for row in BV_in_col]
      
    else:
        # skit to phase II
        z += [0] * n
        A.append(z)

        """Start Phase II when no artif. variables found"""
        column = find_pivot_column(A[-1], len(z))
        while column != len(A[-1]):
            row = find_pivot_row(A, rhs, column, n)
            if row == -1:
                return 1, []
            
            div = A[row][column]
            # relax tableau row
            if div != 1:
                for i in range(n + m):
                    A[row][i] /= div
                rhs[row] /= div

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row and A[j][column]: 
                    div = -A[j][column] / A[row][column]
                    for k in range(n + m):
                        A[j][k] += A[row][k] * div
                    rhs[j] += rhs[row] * div
            if column < m:
                if BV_in_row[row] != float('inf'):
                    BV_in_col[BV_in_row[row]] = float('inf')

                BV_in_col[column] = row
            BV_in_row[row] = column
            
            column = find_pivot_column(A[-1], len(z))

        # break out of the loop, optimal solution found
        return 0, [0 if row == float('inf') else rhs[row] for row in BV_in_col]


if __name__ == '__main__':
    n, m = map(int, input().split())

    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]

    rhs = list(map(int, stdin.readline().split()))
    z = list(map(lambda x: int(x) * (-1), input().split()))

    s, e = [], []
    for i, val in enumerate(rhs):
        if val < 0:
            rhs[i] = -val
            A[i] = [-j for j in A[i]]
            e.append(i)
        else:
            s.append(i)
    
    ln = len(s) + 2 * len(e)
    # construct tableau
    for i, val in enumerate(s):
        aux = [0] * ln
        aux[i] = 1
        A[val] += aux

    w = []
    artif_set = set()
    rhs.append(0)
    if e:
        # if we have artificial variables
        artif_colms = [0] * len(e)
        for i, val in enumerate(e):
            aux = [0] * ln
            aux[len(s) + i] = -1
            ind = len(s) + len(e) + i
            aux[ind] = 1
            artif_colms[i] = ind + m
            A[val] += aux

        # construct W objective function
        w = [0] * len(A[0])
        for row in e:
            rhs[-1] += -rhs[row]
        
        artif_set = set(artif_colms)
        for i in range(len(w)):
            if i not in artif_set:
                for row in e:
                    w[i] += A[row][i] * (-1)
        

    anst, ansx = allocate_ads(n, m, A, rhs, z, w, artif_set)

    if anst == -1:
        print("No solution")
    if anst == 0:  
        print("Bounded solution")
        print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
    if anst == 1:
        print("Infinity")
    
