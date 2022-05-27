# Uses python3
import random


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
        if a[l][0] == a[r][0]:
            if a[l][1] > a[r][1]:
                a[l], a[r] = a[r], a[l]
        else:
            if a[l][0] > a[r][0]:
                a[l], a[r] = a[r], a[l]
        return
    else: 
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        #use partition3
        m1, m2 = partition3(a, l, r, i)

        middle_quick_sort(a, m1, m2, 1)

        randomized_quick_sort(a, l, m1 - 1, i)
        randomized_quick_sort(a, m2 + 1, r, i)


def middle_quick_sort(a, l, r, i):
    if l >= r:
        return
    elif r - l == 1:
        if a[l][i] > a[r][i]:
            a[l], a[r] = a[r], a[l]
        
        return
    else:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r, 1)

        randomized_quick_sort(a, l, m1 - 1, 1)
        randomized_quick_sort(a, m2 + 1, r, 1)


def show_payoffs(line, indexes):

    randomized_quick_sort(line, 0, len(line) - 1, 0)

    payoffs = [0] * len(indexes)
    result = [0] * len(indexes)
    count = j = i = 0

    while j != len(indexes) or i != len(line):
        if line[i][1] == 0:
            count += 1
        elif line[i][1] == 1:
            payoffs[j] = count
            j += 1
        elif line[i][1] == 2:
            count -= 1
        i += 1
    
    for i, value in enumerate(indexes):
        result[value] = payoffs[i]

    return " ".join([str(i) for i in result])


if __name__ == '__main__':
    segments, points = [int(i) for i in input().split()]

    left, bet, right = 0, 1, 2
    line = [0] * 2 * segments + [0] * points
    for i in range(0, 2 * segments, 2):
        a, b = [int(i) for i in input().split()]
        line[i] = (a, left)
        line[i + 1] = (b, right)

    points = [(i, int(v)) for i, v in enumerate(input().split())]
    points_sorted = sorted(points, key=lambda x: x[1])

    points_indexes = [i[0] for i in points_sorted]

    j = 0
    for i in range(2 * segments, 2 * segments + len(points)):
        line[i] = (points[j][1], bet)
        j += 1

    print(show_payoffs(line, points_indexes))