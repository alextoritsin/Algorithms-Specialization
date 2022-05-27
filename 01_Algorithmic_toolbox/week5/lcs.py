# uses python3

def calc_lcs(arr1, arr2, n, m):
    dist = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1] + 1
            else:
                dist[i][j] = max(dist[i - 1][j], dist[i][j - 1])
        
    return dist[i][j]


if __name__ == '__main__':
    n = int(input())
    array1 = [int(i) for i in input().split()]

    m = int(input())
    array2 = [int(i) for i in input().split()]
    
    print(calc_lcs(array1, array2, n, m))

    
