# Uses python3
import random

def partition3(a, l, r):

    # initialize pivots m1 and m2
    m2 = j = l
    x = a[l]

    # sort array: m1 ... m2, then < m2 and > m2
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]

        elif a[i] == x:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]

            if a[i] < x:
                j += 1
                a[j], a[i] = a[i], a[j]
            else:
                j += 1            

    # place m1 ... m2 between left and right parts
    if j > m2:
        for i in range(l, m2 + 1):
            a[i], a[j - i + l] = a[j - i + l], a[i]

    return j - m2 + l, j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    elif r - l == 1:
        a[l], a[r] = min(a[l], a[r]), max(a[l], a[r])
        return
    else:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        #use partition3
        m1, m2 = partition3(a, l, r)
        randomized_quick_sort(a, l, m1 - 1)
        randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]

    randomized_quick_sort(array, 0, n - 1)
    print(" ".join([str(num) for num in array]))
