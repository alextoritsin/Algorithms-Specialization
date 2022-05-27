# uses python3
import sys
import random
import string

from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans


def poly_hash(s, x, p):
    hash = 0
    for i in range(len(s)):
        hash = (hash + ord(s[i]) * pow(x, i, p)) % p
    
    return hash
    

def search_max(max_len, min_str, max_str, x=263, p=10000000007):

    # init hashtables
    hash_min_dict = dict()

    hash_min = [0] * (len(min_str) - max_len + 1)
    hash_max = [0] * (len(max_str) - max_len + 1)

    # def last hashes
    last_hash_min = poly_hash(min_str[-max_len:], x, p)
    last_hash_max = poly_hash(max_str[-max_len:], x, p)
    
    hash_min_dict[last_hash_min] = len(hash_min) - 1
    hash_min[-1] = last_hash_min
    hash_max[-1] = last_hash_max

    # calc multiplier y
    y = pow(x, max_len, p)

    # calc remain hashes of min string
    for i in range(len(hash_max) - 2, len(hash_min) - 2, -1):
        hash_max[i] = (x * hash_max[i + 1] + ord(max_str[i]) - y * ord(max_str[i + max_len])) % p

    for j in range(len(hash_min) - 2, -1, -1):
        hash_min[j] = (x * hash_min[j + 1] + ord(min_str[j]) - y * ord(min_str[j + max_len])) % p
        hash_max[j] = (x * hash_max[j + 1] + ord(max_str[j]) - y * ord(max_str[j + max_len])) % p
        # add hash value to dict
        hash_min_dict[hash_min[j]] = j

    for k in range(len(hash_max)):
        if hash_max[k] in hash_min_dict:
            i = hash_min_dict[hash_max[k]]
            if max_str[k:k + max_len - 1] == min_str[i:i + max_len - 1]:

                return i, k, max_len
   

    return 0, 0, max_len // 2 


def find_max_common(s, t):
    """Using binary search to find length of max
    common substring"""
    l = -1
    r = min(len(s), len(t))
    while r - l != 1:
        index = (r + l) // 2

        max_len = index + 1
        if len(s) <= len(t):
            i, j, res_len = search_max(max_len, s, t)
        else:
            j, i, res_len = search_max(max_len, t, s)

        if res_len == max_len:
            l = index
            ind_s = i
            ind_t = j
        else:
            r = index

    if l == -1:
        # return 0, 0, 0
        print(0, 0, 0)
    else:
        # return ind_s, ind_t, l + 1
        print(ind_s, ind_t, l + 1)


if __name__ == '__main__':
        # s, t = input().split()
        # find_max_common(s, t)

    # letters = string.ascii_lowercase[:3]
    # while True:
    
    #     s_len = random.randint(2, 30)
    #     t_len = random.randint(2, 30)
    #     s = ''.join(random.choice(letters) for i in range(s_len))
    #     t = ''.join(random.choice(letters) for i in range(t_len))
    #     # s, t = input().split()
    #     i, j, my_len = find_max_common(s, t)
    #     # find_max_common(s, t)

    #     ans = solve(s, t)
    #     if my_len != 0:
    #         if s[i:i + my_len - 1] == t[j:j + my_len - 1] and s[ans.i:ans.i + ans.len - 1] == t[ans.j:ans.j + ans.len - 1] and my_len == ans.len:
    #             print(s, t)
    #             print('OK!')
    #         else:
    #             print(s, t)
    #             print("My func:")
    #             print(i, j, my_len)

    #             print("Naive func:")
    #             print(ans.i, ans.j, ans.len)
    #             break

    for line in sys.stdin.readlines():
        s, t = line.split()
        find_max_common(s, t)