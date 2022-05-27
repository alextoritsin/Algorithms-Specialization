# uses python3


def process_query(h_table, query):
    key = int(query[1])
    if query[0] == 'add':
        value = query[2]
        h_table[key] = value
    elif query[0] == 'del':
        if h_table[key]:
            h_table[key] = 0
    elif query[0] == 'find':
        if h_table[key]:
            print(h_table[key])
        else:
            print("not found")


if __name__ == '__main__':
    # use list for hashtable
    hashtable = [0] * 10 ** 8

    # number of queries
    N = int(input())
    for q in range(N):
        query = input().split()
        process_query(hashtable, query)
