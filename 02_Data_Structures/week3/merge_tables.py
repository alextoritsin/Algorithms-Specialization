# uses python3


def find(i):
    if i != tables[i][0]:
        tables[i][0] = find(tables[i][0])
    return tables[i][0]


def get_max_rows(dest, src, rank, tables, max_row):

    dest_id = find(dest - 1)
    src_id = find(src - 1)
    
    if dest_id == src_id:
        # no changes in max rows
        return max_row
    else:
        # check if dest rank more than src rank
        if rank[dest_id] >= rank[src_id]:
            tables[src_id][0] = dest_id
            # if equal increase dest rank
            if rank[dest_id] == rank[src_id]:
                rank[dest_id] += 1
            # copy rows from src to destination
            tables[dest_id][1] += tables[src_id][1]
            tables[src_id][1] = 0
            max_query = tables[dest_id][1]

        else:
            # we found rank src > rank dest
            tables[dest_id][0] = src_id
            tables[src_id][1] += tables[dest_id][1]
            tables[dest_id][1] = 0
            max_query = tables[src_id][1]
        
        max_row = max(max_row, max_query)
            
        return max_row
        

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    tables = [0] * n
    max_row = 0

    for i, num_rows in enumerate(input().split()):
        tables[i] = [i, int(num_rows)]
        max_row = max(max_row, int(num_rows))

    rank = [0] * n

    for q in range(m):
        dest, src = [int(i) for i in input().split()]
        max_row = get_max_rows(dest, src, rank, tables, max_row)
        print(max_row)
        