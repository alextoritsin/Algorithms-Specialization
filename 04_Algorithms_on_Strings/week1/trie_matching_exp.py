# python3
import sys


def build_trie(patterns):
    """Constracts a trie out of the list of patterns"""
    tree = dict()
    tree[0] = dict()
    new_node = 0
    for pat in patterns:
        cur_node = 0
        for char in pat:
			# go down along a branch
            if char in tree[cur_node]:
                cur_node = tree[cur_node][char]
            else:
                # if char not in trie, add it to node
                new_node += 1
                tree[cur_node][char] = new_node
                cur_node = new_node
                # add new empty node
                tree[cur_node] = dict()
        # place sentinel symbol
        tree[cur_node]['$'] = 1

    return tree


def solve (text, patterns):
    """Finds all starting position in `text`,
        where str from `patterns` appears as a substring"""
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        curr_node = 0
        for j in range(i, len(text)):
            char = text[j]
            if char in trie[curr_node]:
                curr_node = trie[curr_node][char]
                # check whether we reach a sentinel symbol
                if '$' in trie[curr_node]:
                    result.append(i)
                    break
            else:
                break

    return result
	

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	patterns = []
	for i in range(n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve(text, patterns)

	sys.stdout.write(' '.join(map(str, ans)) + '\n')
