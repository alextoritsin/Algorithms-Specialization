# python3
from sys import stdin


TOL = 1e-7

def find_pivot_row(A, rhs, col, n):
    
    best_ratio = float('inf')
    row = -1
    for j in range(n):
        if A[j][col] > 0:
            cur_ratio = rhs[j] / A[j][col]
            is_same_ration = (best_ratio - cur_ratio) <= TOL and (best_ratio - cur_ratio) >= 0
            cond = is_same_ration if j < row else cur_ratio < best_ratio
            if cond:
                best_ratio = cur_ratio
                row = j
    
    return row


def find_pivot_column(obj_func, length, rng=set()):
    min_elem = 0
    if rng:
        index = len(rng)
        for i in rng:
            if abs(obj_func[i] - min_elem) > TOL and obj_func[i] < min_elem:
                min_elem = obj_func[i]
                index = i
    else:
        index = length
        for i in range(length):
            if abs(obj_func[i] - min_elem) > TOL and obj_func[i] < min_elem:
                min_elem = obj_func[i]
                index = i
    
    return index


def pivot_tableau(A:list, column:int, row:int, rhs:list,
                  n:int, indecis:list, BV_row, BV_col):
    # normalize row
    div = A[row][column]
    if div != 1:
        for i in indecis:
            A[row][i] = A[row][i] / div + 0
        rhs[row] = rhs[row] / div + 0

    # complete row reduction by elimination
    for j in range(n + 1):
        if j != row and A[j][column]: 
            div = -A[j][column] / A[row][column]
            for k in indecis:
                A[j][k] += A[row][k] * div
            rhs[j] += rhs[row] * div

    # rearrange relation btw row and column of bv
    cur_col = BV_row[row]
    if cur_col != float('inf'):
        BV_col[cur_col] = float('inf')
    
    BV_row[row] = column
    BV_col[column] = row
    
    column = find_pivot_column(A[-1], len(indecis))

    return column, A, rhs, BV_row, BV_col


def allocate_ads(n, m, A:list, rhs, z, w, artif_set, BV_in_row, BV_in_col):
    if w:
        # go to phase One
        A.append(w)
        ln = len(w)
        init_vars = set(range(ln)) - artif_set
        # BV_in_row = [float('inf')] * n
        column = find_pivot_column(A[-1], ln)
        indecis = list(range(ln))
        while column != ln:
            if column < m:
                init_vars -= {column}

            row = find_pivot_row(A, rhs, column, n)
            
            if row == -1:
                return 1, []

            column, A, rhs, BV_in_row, BV_in_col = pivot_tableau(A, column, row, rhs, n, indecis, BV_in_row, BV_in_col)
            # # normalize row
            # div = A[row][column]
            # if div != 1:
            #     for i in range(ln):
            #         A[row][i] = A[row][i] / div + 0
            #     rhs[row] = rhs[row] / div + 0

            # # complete row reduction by elimination
            # for j in range(n + 1):
            #     if j != row and A[j][column]: 
            #         div = -A[j][column] / A[row][column]
            #         for k in range(ln):
            #             A[j][k] += A[row][k] * div
            #         rhs[j] += rhs[row] * div

            # # rearrange relation btw row and column of bv
            # cur_col = BV_in_row[row]
            # if cur_col != float('inf'):
            #     BV_in_col[cur_col] = float('inf')
            
            # BV_in_row[row] = column
            # BV_in_col[column] = row
            
            # column = find_pivot_column(A[-1], ln)


        # check for infeasibility
        if abs(rhs[-1]) > 1e-5:
            return -1, []

        # Iteration if BV is still in artificial variables
        iterated_set = set()
        for column in artif_set:
            if BV_in_col[column] != float('inf'):
                row = BV_in_col[column]
                for col in init_vars:
                    div = A[row][col]
                    if div != 0:
                        # normalize row
                        if div != 1:
                            for i in range(ln):
                                A[row][i] = A[row][i] / div + 0
                            rhs[row] = rhs[row] / div + 0

                        # complete row reduction by elimination
                        for j in range(n):          
                            if j != row and A[j][col]: 
                                div = -A[j][col] / A[row][col]
                                for k in range(ln):
                                    A[j][k] += A[row][k] * div
                                rhs[j] += rhs[row] * div

                        init_vars -= {col}
                        BV_in_col[col], BV_in_col[column] = row, float('inf')
                        BV_in_row[row] = col
                        iterated_set.add(column)
                        break
                else:
                    r = [0] * len(A[0])
                    r[column] = 1
                    rhs[row] = 0
                    A[row] = r
            else:
                # no BV in that column, add it to iterated
                iterated_set.add(column)
            
        # prepare tableau for phase Two
        A[-1] = z + [0] * (ln - m)
        rng = set(range(ln)) - iterated_set
        ln = len(w) - len(artif_set)
        # check columns in z row to be 0 if that column contains BV
        for i in range(m):
        # for i, row in enumerate(BV_in_col):
            if BV_in_col[i] != float('inf') and A[-1][i] != 0:
                scale = A[-1][i] * (-1)
                for k in rng:
                    A[-1][k] += A[BV_in_col[i]][k] * scale
                rhs[-1] += rhs[BV_in_col[i]] * scale


        """Start Phase II"""
        column = find_pivot_column(A[-1], ln, rng)
        while column != len(rng):
            row = find_pivot_row(A, rhs, column, n)

            if row == -1:
                return 1, []
            # normalize row
            div = A[row][column]
            if div != 1:
                for i in rng:
                    A[row][i] = A[row][i] / div + 0
                rhs[row] = rhs[row] / div + 0

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row and A[j][column]: 
                    div = -A[j][column] / A[row][column]
                    for k in rng:
                        A[j][k] += A[row][k] * div
                    rhs[j] += rhs[row] * div

            cur_col = BV_in_row[row]
            if cur_col != float('inf'):
                BV_in_col[cur_col] = float('inf')

            BV_in_row[row] = column
            BV_in_col[column] = row
            
            column = find_pivot_column(A[-1], ln)

        # break out of the loop, optimal solution found
        return 0, [0 if row == float('inf') else rhs[row] for row in BV_in_col[:m]]
      
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
            # normalize row
            if div != 1:
                for i in range(n + m):
                    A[row][i] = A[row][i] / div + 0
                rhs[row] = rhs[row] / div + 0

            # complete row reduction by elimination
            for j in range(n + 1):
                if j != row and A[j][column]: 
                    div = -A[j][column] / A[row][column]
                    for k in range(n + m):
                        A[j][k] += A[row][k] * div
                    rhs[j] += rhs[row] * div
                    
            cur_col = BV_in_row[row]
            if cur_col != float('inf'):
                BV_in_col[cur_col] = float('inf')

            BV_in_row[row] = column
            BV_in_col[column] = row
            
            column = find_pivot_column(A[-1], len(z))

        # break out of the loop, optimal solution found
        return 0, [0 if row == float('inf') else rhs[row] for row in BV_in_col[:m]]


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
    BV_in_col = [float('inf')] * (m + ln)
    BV_in_row = [float('inf')] * n
    if e:
        # if we have artificial variables
        artif_colms = [0] * len(e)
        for i, row in enumerate(e):
            aux = [0] * ln
            aux[len(s) + i] = -1
            ind = len(s) + len(e) + i
            aux[ind] = 1
            artif_colms[i] = ind + m
            A[row] += aux
            BV_in_row[row] = m + ind
            BV_in_col[BV_in_row[row]] = row
            rhs[-1] += -rhs[row]

        # construct W objective function
        w = [0] * len(A[0])
        artif_set = set(artif_colms)
        for i in range(len(w)):
            if i not in artif_set:
                for row in e:
                    w[i] += A[row][i] * (-1)
        

    anst, ansx = allocate_ads(n, m, A, rhs, z, w, artif_set, BV_in_row, BV_in_col)

    if anst == -1:
        print("No solution")
    if anst == 0:  
        print("Bounded solution")
        print(" ".join(["{0:.15f}".format(x) for x in ansx]))
    if anst == 1:
        print("Infinity")
    
