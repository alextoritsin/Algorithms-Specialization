# uses python3
# Problem 1


def sift_down(index:int, size:int, arr:list, swaps:list):
    if 2 * index + 1 >= size:
        return

    min_index = index
    l_child = 2 * index + 1
    r_child = 2 * index + 2

    if l_child < size and arr[l_child] < arr[min_index]:
        min_index = l_child

    if r_child < size and arr[r_child] < arr[min_index]:
        min_index = r_child

    if index != min_index:
        arr[index], arr[min_index] = arr[min_index], arr[index]
        swaps.append((index, min_index))
        sift_down(min_index, size, arr, swaps)


def build_heap(arr, n):
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n, arr, swaps)

    return swaps

if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]

    swaps = build_heap(array, n)
    print(len(swaps))

    if len(swaps):
        for swap in swaps:
            i, j = swap
            print(i, j)
    