# uses python3

def calc_height(nodes, n):
    tree = [[] for k in range(n)]
    for i in range(n):
        parent = nodes[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
            
    queue = [] 
    queue.append(root)
    height = 1

    while len(queue):
        aux = []
        for elem in queue:
            if tree[elem]:
                for item in tree[elem]:
                    aux.append(item)
        queue.clear()

        if len(aux):
            height += 1
            queue = aux.copy()

    return height

if __name__ == '__main__':
    n = int(input())
    nodes = [int(i) for i in input().split()]
    print(calc_height(nodes, n))