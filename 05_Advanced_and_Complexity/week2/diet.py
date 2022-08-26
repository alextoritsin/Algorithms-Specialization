# python3
from sys import stdin
import copy

       
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def SelectPivotElement(a, used_rows, piv_elem:Position, size):
    # init_row = piv_elem.row
    while piv_elem.row < size and (used_rows[piv_elem.row] or abs(a[piv_elem.row][piv_elem.column]) == 0):
        piv_elem.row += 1
    
    # if piv_elem.row == size:
    #     return False


    return piv_elem


def SwapLines(a, b, used_rows, piv_elem:Position):
    a[piv_elem.column], a[piv_elem.row] = a[piv_elem.row], a[piv_elem.column]
    b[piv_elem.column], b[piv_elem.row] = b[piv_elem.row], b[piv_elem.column]
    used_rows[piv_elem.column], used_rows[piv_elem.row] = used_rows[piv_elem.row], used_rows[piv_elem.column]
    piv_elem.row = piv_elem.column


def ProcessPivotElement(a, b, piv_elem:Position, size, used_rows):
    # find divider
    div = a[piv_elem.row][piv_elem.column]
    # make pivot element equals 1
    if div != 1:
        for i in range(piv_elem.column, size):
            a[piv_elem.row][i] /= div
        b[piv_elem.row] /= div

     # substruct pivot row from every other row to make 0 in pivot column
    for i in range(size):
        mult = a[i][piv_elem.column]
        if i == piv_elem.row or mult == 0:
            continue
        else:
            # substruct 'row' from every row
            for j in range(size):
                a[i][j] -= a[piv_elem.row][j] * mult
            b[i] -= b[piv_elem.row] * mult
                
    used_rows[piv_elem.row] = True

    return piv_elem


def SolveEquation(a, b):
    """
    Solves system of linear equations represented by square matrix 'a'
    and vector 'b' using Gauss Jordan Elimination method
    """
    size = len(a)

    used_rows = [False] * size
    for step in range(size):
        piv_elem = Position(step, 0)
        piv_elem = SelectPivotElement(a, used_rows, piv_elem, size)

        if piv_elem.row == size:
            if b[step] != 0:
                return None
            else:
                b[piv_elem.column] = 0
        # if not piv_elem:
        #     b[piv_elem.column] = 0
        #     continue

            # return None
        SwapLines(a, b, used_rows, piv_elem)
        piv_elem = ProcessPivotElement(a, b, piv_elem, size, used_rows)

    return b


def combination_indicies(n, k, j=0, stack=[]):
    """https://stackoverflow.com/a/66754344/16522852"""
    if len(stack) == k:            
        yield set(stack)
        return
        
    for i in range(j, n): 
        stack.append(i)
        for x in combination_indicies(n, k, i + 1, stack):            
            yield x
        stack.pop()  


def get_square_matrix(A, b, indices):
    A_copy = copy.deepcopy(A)
    matrix = [0] * len(indices)
    b_vector = [0] * len(indices)
    for i, index in enumerate(indices):
        matrix[i] = A_copy[index]

        b_vector[i] = b[index]

    return matrix, b_vector


def solve_diet_problem(n, m, A, b:list, c:list):
    max_pleasure = float('-inf')
    last_index = -1
    result = []
    whole_set = set(range(n + m + 1))
    m_set = set(range(n, n + m))

    for k_set in (combination_indicies(n + m + 1, m)):
        # A_copy = copy.deepcopy(A)
        # b_copy
        # get small matrix using indecis from 'k_set'
        matrix, b_vector = get_square_matrix(A, b, k_set)
        
        # result for every other inequalities
        res = SolveEquation(matrix, b_vector)
        # check that all values not negative
        if res:
            for x in res:
                if x < 0:
                    break
            else:
                for index in whole_set - k_set:
                    if index not in m_set:
                        ans = 0
                        for x in range(m):
                            ans += A[index][x] * res[x]
                        if ans > b[index] + 1e-3: 
                            # ineq. in matrix A in 'A[index]' doesn't satisfied
                            break

                else:
                    # all inequalitions satisfied, we found solution
                    pleasure = 0
                    # calculate pleasure
                    for i in range(m):
                        pleasure += c[i] * res[i]
                    if pleasure > max_pleasure:
                        max_pleasure = pleasure
                        last_index = 1 if (n + m) in k_set else 0
                        result = res


    return last_index, result


if __name__ == '__main__':
    
    n, m = list(map(int, stdin.readline().split()))

    # construct big matrix of size 'n + m + 1'
    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]

    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))

    for i in range(m):
        exp = [0] * m
        exp[i] = 1
        A.append(exp)
        b.append(0)

    A.append([1] * m)
    b.append(pow(10, 9))

    anst, ansx = solve_diet_problem(n, m, A, b, c)

    if anst == -1:
        print("No solution")
    if anst == 0:  
        print("Bounded solution")
        print(" ".join(["{0:.15f}".format(x) for x in ansx]))
        # print(' '.join(list(map(lambda x : "{0:.15f}".format(x)))))

    if anst == 1:
        print("Infinity")
    
