# uses python3
from collections import deque


def process_packets(packets, S, n):
    if n == 0:
        return

    queue = deque()

    for packet in packets:
        if not len(queue):
            queue.append((packet[0], sum(packet)))
            print(packet[0])
        else:
            while len(queue) and queue[0][1] <= packet[0]:
                queue.popleft()

            if len(queue):
                if len(queue) < S:
                    last_time = queue[-1][1] + packet[1]
                    queue.append((queue[-1][1], last_time))
                    print(queue[-1][0])
                else:
                    print(-1)
            else:
                queue.append((packet[0], sum(packet)))
                print(packet[0])
        


if __name__ == '__main__':
    S, n = [int(i) for i in input().split()]

    packets = [0] * n
    for i in range(n):
        t, p = list(map(lambda x: int(x), input().split()))
        packets[i] = (t, p)

    process_packets(packets, S, n)
    