#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    """Constracts a trie out of the list of patterns"""
    tree = dict()
    tree[0] = dict()
    new_node = 0
    for pat in patterns:
        cur_node = 0
        for char in pat:
            if cur_node not in tree:
                tree[cur_node] = dict()
            if char in tree[cur_node]:
                cur_node = tree[cur_node][char]
            else:
                new_node += 1
                tree[cur_node][char] = new_node
                cur_node = new_node

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
