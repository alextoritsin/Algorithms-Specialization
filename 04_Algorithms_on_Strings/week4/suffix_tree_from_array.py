# python3
import sys


class Node:
    def __init__(self, id:int, parent:'Node', children:dict, label:list, depth:int):
        self.id = id
        self.parent = parent
        self.children = children
        self.label = label
        self.depth = depth
    

def print_edges(root:Node, nodes:int):
    """Prints all edges of suffix tree rooted in 'root'
    with 'nodes' number of nodes using iterible DFS
    in ascending order without repeated nodes"""
    stack = []
    keys = ['T', 'G', 'C', 'A', '$']
    marked = [False] * nodes
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        if len(node.label):
            print(" ".join([str(i) for i in node.label]))
        if len(node.children):
            id = 0
            marked[node.id] = True
            childs = node.children
            ln = len(childs)
            while ln > 0:
                if keys[id] in childs:
                    stack.append(childs[keys[id]])
                    ln -= 1
                id += 1


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    tree = {} 
    n = len(text)
    # create root node
    root = Node(0, None, dict(), [], 0)
    # create frst suf node with $
    node_1 = Node(1, root, dict(), [sa[0], n], 1)
    root.children[text[sa[0]]] = node_1
    id = 1
    for i in range(1, len(sa)):
        suf_ind = sa[i]
        pref = lcp[i - 1]
        if pref == 0:
            id += 1
            new_node = Node(id, root, dict(), [suf_ind, n], n - suf_ind)
            root.children[text[suf_ind]] = new_node
            curr_node = new_node
        else:
            while curr_node.depth > pref:
                curr_node = curr_node.parent
            depth = curr_node.depth
            index = suf_ind + curr_node.depth 
            # check if suf (with index 'index') of suf in curr node children
            if text[index] not in curr_node.children:
                id += 1
                new_node = Node(id, curr_node, dict(), [index, n], depth + n - index)
                curr_node.children[text[index]] = new_node
                curr_node = new_node
            else:
                child = curr_node.children[text[index]]
                # if child of curr node has children  
                if len(child.children):
                    label = [child.label[0], child.label[0] + pref - depth]
                    # create middle node
                    id += 1
                    middle_node = Node(id, curr_node, dict(), label, pref)
                    middle_node.children[text[label[1]]] = child

                    # change parent node child, curr node parent and link from parent to child
                    child.label[0] = middle_node.label[1]
                    curr_node.children[text[label[0]]] = middle_node
                    child.parent = middle_node

                    # create node for what is left from new suffix
                    id += 1
                    new_node = Node(id, middle_node, dict(), [suf_ind + pref, n], n - suf_ind)
                    middle_node.children[text[suf_ind + pref]] = new_node
                    curr_node = new_node
                    
                # if child of curr node has no children
                else:
                    # chenging existing siffix
                    # change child props
                    label = [child.label[0], child.label[0] + pref - depth]
                    child.label = label
                    # create new node
                    id += 1
                    break_node = Node(id, child, dict(), [label[1], n], child.depth)
                    # change the depth of child node
                    child.depth = curr_node.depth + label[1] - label[0]
                    # add break_node as child
                    child.children[text[label[1]]] = break_node

                    # adding node for new suffix
                    id += 1
                    new_node = Node(id, child, dict(), [suf_ind + pref, n], n - suf_ind)
                    # add new node as child
                    child.children[text[new_node.label[0]]] = new_node
                    # reassign current node
                    curr_node = new_node
    
    return root, id + 1


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    root, nodes = suffix_array_to_suffix_tree(sa, lcp, text)
    print_edges(root, nodes)
