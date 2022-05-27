# uses python3


def calc_edit_distance(str1, str2):
    n, m = len(str1), len(str2)
    dist = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][0] = i
    
    for i in range(1, m + 1):
        dist[0][i] = i
    
    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            insrt = dist[i][j - 1] + 1
            delt = dist[i - 1][j] + 1
            if str1[i - 1] == str2[j - 1]:
                char_match = dist[i - 1][j - 1]
            else:
                char_match = dist[i - 1][j - 1] + 1

            dist[i][j] = min(insrt, delt, char_match)

    return dist[n][m]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(calc_edit_distance(str1, str2))