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

    if size == 0:
        exit(0)
    elif size == 1:
        print(b[0] / a[0])
        exit(0)

    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns, piv_elem:Position, size):
    while used_rows[piv_elem.row] or not a[piv_elem.row][piv_elem.column]:
        piv_elem.row += 1
    # piv_elem = Position(0, 0)
    # while used_columns[piv_elem.column]:
    #     piv_elem.column += 1
    # while used_rows[piv_elem.row]:
    #     piv_elem.row += 1

    # while not a[piv_elem.row][piv_elem.column]:
    #     if piv_elem.column + 1 < size and used_columns[piv_elem.column]:
    #         piv_elem.column += 1
    #     elif piv_elem.row + 1 < size:
    #         piv_elem.row += 1
    #     else:
    #         used_columns[piv_elem.column] = True
    #         break

    return piv_elem


def SwapLines(a, b, used_rows, piv_elem:Position):
    a[piv_elem.column], a[piv_elem.row] = a[piv_elem.row], a[piv_elem.column]
    b[piv_elem.column], b[piv_elem.row] = b[piv_elem.row], b[piv_elem.column]
    used_rows[piv_elem.column], used_rows[piv_elem.row] = used_rows[piv_elem.row], used_rows[piv_elem.column]
    piv_elem.row = piv_elem.column


def ProcessPivotElement(a, b, piv_elem:Position, size, used_rows):
    # find divider and pivot row
    row = a[piv_elem.row]
    div = a[piv_elem.row][piv_elem.column]
    # make pivot element equals 1
    if div != 1:
        a[piv_elem.row] = [num / div for num in row]

        b[piv_elem.row] = b[piv_elem.row] / div
        row = a[piv_elem.row]


    # substruct pivot row from every other row to make 0 in pivot column
    for i in range(size):
        if i != piv_elem.row:
            # define multiplier
            mult = a[i][piv_elem.column]
            if mult:
                # substruct 'row' from every row
                for j in range(piv_elem.column, size):
                    a[i][j] -= row[j] * mult
                b[i] -= b[piv_elem.row] * mult
                
    # piv_elem.proc.add(piv_elem.row)
    # # increase pivot element
    # piv_elem.row += 1
    # piv_elem.column += 1
    used_rows[piv_elem.row] = True

    return piv_elem


# def MarkPivotElementUsed(piv_elem:Position, used_rows, used_columns):
#     used_rows[piv_elem.row] = True
#     used_columns[piv_elem.column] = True


def SolveEquation(equation:Equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    # while piv_elem.row < size and piv_elem.column < size:
    for step in range(size):
        piv_elem = Position(step, 0)
        # piv_elem.column = step
        piv_elem = SelectPivotElement(a, used_rows, used_columns, piv_elem, size)
        # if not a[piv_elem.row][piv_elem.column]:
        #     continue
        SwapLines(a, b, used_rows, piv_elem)
        piv_elem = ProcessPivotElement(a, b, piv_elem, size, used_rows)
        # MarkPivotElementUsed(piv_elem, used_rows, used_columns)

    return b


# def PrintColumn(column):
    # size = len(column)
    # print("{0:.6f}".format(column[row]), sep=' ', end='\n')
    # for row in range(size):
        # if used_columns[row] and used_rows[row]:
        # else:
        #     print(0, end=' ')
        # # print("%.20lf" % column[row])
    # print()

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    print(" ".join(["{0:.6f}".format(ans) for ans in solution]))
    # PrintColumn(solution)
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