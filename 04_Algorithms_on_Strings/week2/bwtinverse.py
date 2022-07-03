# python3
import sys
from collections import deque

def InverseBWT(bwt):
    """Reconstructs a string from it's
       Burrow-Wheeler Transform"""
    first_col = sorted(bwt)    
    first_col_d = dict()
    last_col_d = dict()
    full_matrix = dict()
    for i, char in enumerate(first_col):
        # get the key out of the first col char
        if char in first_col_d:
            first_col_d[char] += 1
            num_f = first_col_d[char]
        else:
            num_f = 1
            first_col_d[char] = num_f

        # get the value out of the BWT
        if bwt[i] in last_col_d:
            last_col_d[bwt[i]] += 1
            num_bwt = last_col_d[bwt[i]]
        else:
            num_bwt = 1
            last_col_d[bwt[i]] = num_bwt
        # construct associations btw first and last colms
        full_matrix[char + str(num_f)] = bwt[i] + str(num_bwt)

    # get the string using first-last property
    char = '$1'
    string = deque()
    while full_matrix[char] != '$1':
        char = full_matrix[char]
        string.appendleft(char[0])
        
    return "".join(string) + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))