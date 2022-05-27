# uses python3


def calc_lcs(arr1, arr2, arr3, n, m, l):
    dist = [[[0] * (m + 1) for i in range(n + 1)] for j in range(l + 1)]
    for l in range(1, l + 1):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                    if arr1[i - 1] == arr2[j - 1] == arr3[l - 1]:
                        dist[l][i][j] = dist[l - 1][i - 1][j - 1] + 1

                    else:
                        dist[l][i][j] = max(dist[l - 1][i][j], 
                                            dist[l][i - 1][j],
                                            dist[l][i][j - 1])
                
    return dist[l][i][j]


if __name__ == '__main__':
    n = int(input())
    array1 = [int(i) for i in input().split()]
    
    m = int(input())
    array2 = [int(i) for i in input().split()]
    
    l = int(input())
    array3 = [int(i) for i in input().split()]

    print(calc_lcs(array1, array2, array3, n, m, l))
    