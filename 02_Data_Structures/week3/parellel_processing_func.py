# uses python3


def get_index_time(heap, job_time):
    time, index = heap[0]

    print(index, time)

    heap[0] = (time + job_time, index)

    min_index = index = 0
    while 2 * index + 1 < len(heap):

        l_child = 2 * index + 1
        r_child = 2 * index + 2

        if l_child < len(heap) and heap[l_child] < heap[min_index]:
            min_index = l_child

        if r_child < len(heap) and heap[r_child] < heap[min_index]:
            min_index = r_child

        if index != min_index:
            heap[index], heap[min_index] = heap[min_index], heap[index]
            index = min_index
        else:
            break


if __name__ == '__main__':
    threads, _ = [int(i) for i in input().split()]

    heap = [(0, i) for i in range(threads)]
    jobs = [int(i) for i in input().split()]

    for job in jobs:
        get_index_time(heap, job)