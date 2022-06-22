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
			# add node if node id not in trie
            if cur_node not in tree:
                tree[cur_node] = dict()
			# go down along a branch
            if char in tree[cur_node]:
                cur_node = tree[cur_node][char]
			# add new value to the node
            else:
                new_node += 1
                tree[cur_node][char] = new_node
                cur_node = new_node

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
				if curr_node not in trie:
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
