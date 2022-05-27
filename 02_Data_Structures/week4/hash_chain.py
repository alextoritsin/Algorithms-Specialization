# uses python3

from collections import deque


def process_query(N, hash_table, x=263, p=1000000007):
    for q in range(N):
        query = input().split()
        cmd = query[0]
        value = query[1]
        if cmd == 'check':
            chain = hash_table[int(value)]
            if chain:
                print(" ".join(chain))
            else:
                print()
        else:   
            # calc hash value
            hash = 0
            for i in range(len(value)):
                hash = (hash + ord(value[i]) * x ** i) % p
            hash = hash % len(hash_table)

            chain = hash_table[hash]
            
            if cmd == 'add':
                if type(chain) != int:
                    if value not in chain:
                        chain.appendleft(value)
                else:
                    chain = deque()
                    chain.appendleft(value)
                    hash_table[hash] = chain
            elif cmd == 'del':
                if chain:
                    try:
                        chain.remove(value)
                    except ValueError:
                        continue
                else:
                    continue
            elif cmd == 'find':
                if chain:
                    print('yes') if value in chain else print('no')
                else:
                    print('no')

    
if __name__ == '__main__':
    # def cardinality
    m = int(input())
    hash_table = [0] * m

    # get number of queries
    N = int(input())

    process_query(N, hash_table)

