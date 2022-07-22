# python3
import sys
from queue import Queue


def build_suffix_tree(text, len_t1): 
            
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    tree = dict()
    tree[0] = dict()
    new_node = 0
    for i in range(len(text)):
        if i < len_t1:
            first = True
        elif i > len_t1:
            first = False
        str_type = {'A'} if first else {'B'}    

        cur_node = 0
        pat_ind = i
        char = text[pat_ind]

        if char in tree[cur_node]:
            while char in tree[cur_node]:
                break_ind = pat_ind
                (lab, str_ind, length, node) = tree[cur_node][char]
                end = str_ind + length
                for j in range(str_ind, end):
                    if text[j] == text[pat_ind]:
                        pat_ind += 1
                    else:
                        break_ind = pat_ind
                        break
                # check if get throught all edge
                if break_ind != pat_ind:
                    # lab |= str_type
                    tree[cur_node][char] = (lab | str_type, str_ind, length, node)
                    cur_node = node                    
                    char = text[pat_ind]
                else:
                    # case when node don't have outcoming edges
                    if not len(tree[node]):
                        # update the edge with decreased length
                        label = tree[cur_node][char][0]
                        tree[cur_node][char] = (label | str_type, str_ind, j - str_ind, node)
                        # create node and add left edge length
                        new_node += 1
                        tree[new_node] = dict()
                        tree[node][text[j]] = (label, j, len(text) - j, new_node)
                        # create node and add left suffix
                        new_node += 1
                        tree[node][text[pat_ind]] = (str_type, pat_ind, len(text) - pat_ind, new_node)
                        tree[new_node] = dict()
                    # case when node have outcoming edges
                    else:
                        # create middle node and update edge to it
                        label = tree[cur_node][char][0] | str_type
                        new_node += 1
                        tree[new_node] = dict()
                        tree[cur_node][char] = (label, str_ind, j - str_ind, new_node)
                        # draw the edge from new node to 'node'
                        tree[new_node][text[j]] = (label, j, length - (j - str_ind), node)
                        # draw the edge from new node with left suffix
                        tree[new_node][text[pat_ind]] = (str_type, pat_ind, len(text) - pat_ind, new_node + 1)
                        new_node += 1
                        tree[new_node] = dict()
                    break
            # used when no node from curr node with letter char
            if char not in tree[cur_node]:
                new_node += 1
                tree[new_node] = dict()
                tree[cur_node][text[pat_ind]] = (str_type, pat_ind, len(text) - pat_ind, new_node)
        
        else:
            new_node += 1
            tree[new_node] = dict()
            tree[cur_node][char] = (str_type, i, len(text) - i, new_node)
    
    return tree


def get_min_non_shared_str(tree, text1, text):
    """
    Returns shortest str of 'text1' that does
    not appear in 'text2'
    """
    n = len(text1)
    prev = [0] * len(tree)
    min_str = text1
    ltr = 'A'
    q = Queue()
    # put root node with id 0 to queue
    q.put(0)
    while not q.empty():
        node = q.get()
        # check every outgoing edge
        for key in tree[node]:
            edge = tree[node][key]
            prev[edge[3]] = (node, key)
            # inside condition we have potent. last node
            if edge[0] == {ltr} and edge[1] < n:
                s = get_str(text, edge[3], prev, tree)
                min_str = s if len(s) < len(min_str) else min_str
            # node not last, adding it to queue
            elif edge[1] < n:
                q.put(edge[3])
    
    return min_str


def get_str(text, node, prev, tree):
    """
    Constructs string from node 0 to node 'node'
    """
    res = ''
    while node != 0:
        last = node
        (node, key) = prev[node]
        (_, start, ln, __)= tree[node][key]
        # when node is not leaf, append all str
        if len(tree[last]):
            res = text[start:start + ln] + res
        else:
        # when node is a leaf, append only first char
            res = text[start]
        
    return res


if __name__ == '__main__':
    text1 = sys.stdin.readline().strip()
    text2 = sys.stdin.readline().strip()
    res = text1 + '#' + text2 + '$'
    tree = build_suffix_tree(res, len(text1))
    print(get_min_non_shared_str(tree, text1, res))




    
            