# python3
import copy

import math
from random import randrange


EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])

    return Equation(a, b)


def SelectPivotElement(a, used_rows, piv_elem:Position, size):
    while piv_elem.row < size and (used_rows[piv_elem.row] or abs(a[piv_elem.row][piv_elem.column]) < EPS):
        piv_elem.row += 1
    
    if piv_elem.row == size:
        return False

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


def SolveEquation(equation:Equation):
    """
    Solves system of linear equations represented by square matrix 'a'
    and vector 'b' using Gauss Jordan Elimination method
    """
    a = equation.a
    b = equation.b
    size = len(a)

    used_rows = [False] * size
    for step in range(size):
        piv_elem = Position(step, 0)
        piv_elem = SelectPivotElement(a, used_rows, piv_elem, size)
        if not piv_elem:
            return None
        SwapLines(a, b, used_rows, piv_elem)
        piv_elem = ProcessPivotElement(a, b, piv_elem, size, used_rows)

    return b


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    print(" ".join(["{0:.6f}".format(ans) for ans in solution]))
    exit(0)


    # """Stress testing"""

    # while True:
    #     """manual input"""
    #     equation = ReadEquation()        
    #     matrix = equation.a
    #     res = equation.b
    #     n = len(matrix)


    #     # """random input"""
    #     # # n = 4
    #     # # matrix = [[0] * n for i in range(n)]
    #     # # res = [0] * n
    #     # # for i in range(n):
    #     # #     for j in range(n): 
    #     # #         matrix[i][j] = randrange(-6, 9, 2)

    #     # # for i in range(n):
    #     # #     res[i] = randrange(-10, 11, 2)


    #     mat_copy = copy.deepcopy(matrix)
    #     res_copy = res.copy()

    #     equation = Equation(matrix, res)
    #     column = SolveEquation(equation)
    #     for i, exp in enumerate(mat_copy):
    #         ans = 0
    #         for j in range(n):
    #             ans += exp[j] * column[j]

    #         close = math.isclose(ans, res_copy[i], rel_tol=0.02)
    #         if not close:
    #             print('Values not too close!')
    #             print(n)
    #             for i, exp in enumerate(mat_copy):
    #                 print(" ".join([str(k) for k in exp]), res_copy[i])
    #             print(column)
    #             exit(0)

    #     print('All values OK!')    