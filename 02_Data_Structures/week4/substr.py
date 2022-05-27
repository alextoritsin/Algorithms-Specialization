# uses python3
import random


def check_equality(a, b, l, x, h1, h2, m1, m2):
    """Compare 2 substrings of string s with
    indexes (a, l), (b, l).
    Input: string s
    Output: "Yes" if equal, else "no" """
    y1 = pow(x, l, m1)
    y2 = pow(x, l, m2)

    hash_a_l_1 = (h1[a + l] - (h1[a] * y1)) % m1
    hash_a_l_2 = (h2[a + l] - (h2[a] * y2)) % m2
    hash_b_l_1 = (h1[b + l] - (h1[b] * y1)) % m1
    hash_b_l_2 = (h2[b + l] - (h2[b] * y2)) % m2

    if hash_a_l_1 == hash_b_l_1 and hash_a_l_2 == hash_b_l_2:
        print('Yes')
        # return 'Yes'
    else:
        print('No')
        # return 'No'


if __name__ == '__main__':
    s = input()    
    q = int(input())

    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9

    h1 = [0] * (len(s) + 1)
    h2 = [0] * (len(s) + 1)
    x = random.randint(1, 10 ** 9)

    for i in range(1, len(s) + 1):
            h1[i] = (x * h1[i - 1] + ord(s[i - 1])) % m1
            h2[i] = (x * h2[i - 1] + ord(s[i - 1])) % m2

    for i in range(q):
        a, b, l = [int(j) for j in input().split()]        
        check_equality(a, b, l, x, h1, h2, m1, m2)

        
