# Uses python3

def merge_sort_count(array):
    n = len(array)
    if n <= 1:
        return 0
    mid = n // 2

    left_part = [array[i] for i in range(mid)]
    right_part = [array[i] for i in range(mid, n)]

    count_left = merge_sort_count(left_part)
    count_right = merge_sort_count(right_part)

    result, merge_count = merge(left_part, right_part) 

    count = 0

    for i in range(n):
        array[i] = result[i]

    count = count + merge_count + count_left + count_right

    return count

def merge(a:list, b:list):
    c = [0] * (len(a) + len(b))
    merge_count = 0
    i = k = n = 0    
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = b[k]
            merge_count += k + len(a) - n
            k += 1
        n += 1

    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1

    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1

    return c, merge_count


if __name__ == '__main__':

    n = int(input())
    array = [int(i) for i in input().split()]

    print(merge_sort_count(array))
    
    
    