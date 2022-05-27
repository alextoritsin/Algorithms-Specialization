# Uses python3

def count_points(sets, n):
    points = []
    i = 0
    while i < n - 1:

        if sets[i][1] >= sets[i + 1][0]:
            sets[i + 1] = [max(sets[i][0], sets[i + 1][0]), min(sets[i][1], sets[i + 1][1])]
            
        else:
            points.append(sets[i][1])
        
        i += 1

    points.append(sets[i][1])
    
    return [str(i) for i in points]

if __name__ == '__main__':
    n = int(input())
    sets = [0] * n

    for i in range(n):
        sets[i] = list(map(int, input().split()))
    
    sets = sorted(sets, key=lambda item: item[0])
    points = count_points(sets, n)
    print(len(points))
    print(" ".join(points))
    