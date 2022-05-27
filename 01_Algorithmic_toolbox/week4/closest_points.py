# Uses python3
import random
import math


# def naive_closest(points, n):
#     d = math.inf
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             d = min(d, calc_distance(points, i, j))

#     return round(d, 4)


def partition3(a, l, r, k):

    # initialize pivots m1 and m2
    m2 = j = l
    x = a[l][k]

    # sort array: m1 ... m2, then < m2 and > m2
    for i in range(l + 1, r + 1):
        if a[i][k] < x:
            j += 1
            a[i], a[j] = a[j], a[i]

        elif a[i][k] == x:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]

            if a[i][k] < x:
                j += 1
                a[j], a[i] = a[i], a[j]
            else:
                j += 1            

    # place m1 ... m2 between left and right parts
    if j > m2:
        for i in range(l, m2 + 1):
            a[i], a[j - i + l] = a[j - i + l], a[i]

    return j - m2 + l, j


def randomized_quick_sort(a, l, r, i):
    if l >= r:
        return
    elif r - l == 1:
        if a[l][i] > a[r][i]:
            a[l], a[r] = a[r], a[l]
        return
    else: 
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r, i)

        randomized_quick_sort(a, l, m1 - 1, i)
        randomized_quick_sort(a, m2 + 1, r, i)


def calc_distance(a:list, i, j):
    return math.sqrt((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2)


def find_closest(a_x:list, a_y:list, l, r):
    if r - l <= 2:
        d = math.inf
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                d = min(d, calc_distance(a_x, i, j)) 

        return round(d, 4)

    mid = (r + l) // 2
    mid_x = (a_x[mid + 1][0] + a_x[mid][0]) / 2

    y_left = []
    y_right = [] 
    for i in range(len(a_y)):
        if a_y[i][0] <= mid_x:
            y_left.append(a_y[i])
        else:
            y_right.append(a_y[i])

    d1 = find_closest(a_x, y_left, l, mid)
    d2 = find_closest(a_x, y_right, mid, r)
    d = min(d1, d2)

    left_bound, right_bound = mid_x - d, mid_x + d
    a_y_middle = list(filter(lambda p: left_bound <= p[0] <= right_bound, a_y))

    for i in range(len(a_y_middle)):
        for j in range(i + 1, min(i + 8, len(a_y_middle))):
            d_y = calc_distance(a_y_middle, i, j)
            if d_y >= d:
                break
            d = min(d, d_y)

    return round(d, 4)

if __name__ == '__main__':
    
    n = int(input())
    points = [0] * n

    for i in range(n):
        a, b = [int(i) for i in input().split()]
        points[i] = (a, b)

    points_y = points.copy()
    points_x = points.copy()

    randomized_quick_sort(points_x, 0, len(points) - 1, 0)
    randomized_quick_sort(points_y, 0, len(points) - 1, 1)

    print(find_closest(points_x, points_y, 0, len(points) - 1))


    # for i in range(10):
            
        # points = [(-4, -3), (-1, 2), (-3, -7), (3, -8), (-8, 10), (-5, 10), (1, -1), (-7, -1)]
        # points = [(-4, -3), (-8, 10), (-5, 10), (-7, -1)]
        # points = [(7, 10), (-2, 1), (-10, -1), (9, 9)]
        # points_y = points.copy()
        # points_x = points.copy()


    # while True:

    # for i in range(10):

    #     n = random.randint(2, 15)
    #     points = [0] * n
    #     for i in range(n):
    #         a = random.randint(-10, 10)
    #         b = random.randint(-10, 10)
    #         points[i] = (a, b)

    #     naive = naive_closest(points, n)

    #     points_x = points.copy()
    #     points_y = points.copy()

    #     randomized_quick_sort(points_x, 0, len(points) - 1, 0)
    #     randomized_quick_sort(points_y, 0, len(points) - 1, 1)

    #     main_func = find_closest(points_x, points_y, 0, n - 1)
    #     if naive != main_func:
    #         print("Error!")
    #         print(points)
    #         print("Naive method:", naive)
    #         print("Main func:", main_func)
    #         break
    #     else:
    #         print("OK!")



