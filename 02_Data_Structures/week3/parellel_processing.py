# uses python3

class Heap:
    def __init__(self, threads):
        self.values = [(0, i) for i in range(threads)]
        self.size = threads
        
    def sift_down(self):
        """Push element to the leafs of the tree"""

        min_index = index = 0
        while 2 * index + 1 < self.size:

            l_child = 2 * index + 1
            r_child = 2 * index + 2

            if l_child < self.size and self.values[l_child] < self.values[min_index]:
                min_index = l_child

            if r_child < self.size and self.values[r_child] < self.values[min_index]:
                min_index = r_child

            if index != min_index:
                self.values[index], self.values[min_index] = self.values[min_index], self.values[index]
                index = min_index
            else:
                break

    def get_free_thread(self):
        """Get the root of the tree based on time execution"""

        return self.values[0][1], self.values[0][0]

    def update_process(self, job_time):
        time, index = self.values[0]
        self.values[0] = (time + job_time, index)
        self.sift_down()


if __name__ == '__main__':
    threads, num_jobs = [int(i) for i in input().split()]
    heap = Heap(threads)
    jobs = [int(i) for i in input().split()]

    for job in jobs:
        index, time = heap.get_free_thread()
        print(index, time)
        heap.update_process(job)
