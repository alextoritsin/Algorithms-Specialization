# python3
import sys
from queue import Queue


def build_suffix_tree(text): 
            
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    tree = dict()
    tree[0] = dict()
    new_node = 0
    for i in range(len(text)):
        cur_node = 0
        pat_ind = i
        char = text[pat_ind]

        if char in tree[cur_node]:
            while char in tree[cur_node]:
                break_ind = pat_ind
                (str_ind, length, node) = tree[cur_node][char]
                end = str_ind + length
                for j in range(str_ind, end):
                    if text[j] == text[pat_ind]:
                        pat_ind += 1
                    else:
                        break_ind = pat_ind
                        break
                # check if get throught all edge
                if break_ind != pat_ind:
                    cur_node = node                    
                    char = text[pat_ind]
                else:
                    # case when node don't have outcoming edges
                    if not len(tree[node]):
                        # update the edge with decreased length
                        tree[cur_node][char] = (str_ind, j - str_ind, node)
                        # create node and add left edge length
                        new_node += 1
                        tree[new_node] = dict()
                        tree[node][text[j]] = (j, len(text) - j, new_node)
                        # create node and add left suffix
                        new_node += 1
                        tree[node][text[pat_ind]] = (pat_ind, len(text) - pat_ind, new_node)
                        tree[new_node] = dict()
                    # case when node have outcoming edges
                    else:
                        # create intermediate node and update edge to it
                        new_node += 1
                        tree[new_node] = dict()
                        tree[cur_node][char] = (str_ind, j - str_ind, new_node)
                        # draw the edge from new node to 'node'
                        tree[new_node][text[j]] = (j, length - (j - str_ind), node)
                        # draw the edge from new node with left suffix
                        tree[new_node][text[pat_ind]] = (pat_ind, len(text) - pat_ind, new_node + 1)
                        new_node += 1
                        tree[new_node] = dict()
                    break
            # used when no node from curr node with letter char
            if char not in tree[cur_node]:
                new_node += 1
                tree[new_node] = dict()
                tree[cur_node][text[pat_ind]] = (pat_ind, len(text) - pat_ind, new_node)
        
        else:
            new_node += 1
            tree[new_node] = dict()
            tree[cur_node][char] = (i, len(text) - i, new_node)
    
    return tree



def get_non_shared(tree:set, q:Queue, min_ind:list, start:int, 
                   len_text:int, len_text1:int, prev:list):
    last_node = float('inf')
    min_ind[0]['skip'] = True 
    found = False
    while not q.empty():
        node = q.get()
        for edge in tree[node]:
            (s, length, t) = tree[node][edge]
            if s < len_text1:
                if not found:
                    min_ind[node] = dict()
                    min_ind[node][edge] = t
                    prev[t] = node
                if s + length == len_text:
                    found = True
                    last_node = t
                else:
                    q.put(t)
            elif s > len_text1 and min_ind[0]['skip']:
                min_ind[0]['skip'] = False

    return None if not found else min_ind


if __name__ == '__main__':
    text1 = sys.stdin.readline().strip()
    text2 = sys.stdin.readline().strip()
    res = text1 + '#' + text2 + '$'
    tree = build_suffix_tree(res)
    q = Queue()
    q.put(0)
    prev = [float('inf')] * len(tree)
    

    last_node = float('inf')
    found = False
    min_str = dict()
    non_skip_node = set()
    while not q.empty():
        node = q.get()
        # if len(tree[node]):
        for edge in tree[node]:
            (s, length, t) = tree[node][edge]
            if s < len(text1):
                # if not found:
                min_str[t] = (s, node)
                    # prev[t] = node
                if s + length == len(res) and not found:
                    found = True
                    last_node = t
                    # break
                else:
                    if len(tree[t]):
                        q.put(t)
            elif s > len(text1) and node in min_str:
                non_skip_node.add(node)

    # collect non-skip nodes
    nodes = non_skip_node.copy()
    for node in nodes:
        while True:
            index, source = min_str[node]
            if source not in non_skip_node:
                if source == 0:
                    break
                else:
                    non_skip_node.add(source)
                    node = source
            else:
                break
        
    # traverse back to 0 node and get min string
    can_skip = True
    string = []
    while last_node != 0:
        index, source = min_str[last_node]
        if source in non_skip_node:
            can_skip = False
        string.append(index)
        last_node = source
    print(text1[string[-1]] if can_skip else "".join([text1[string[i]] for i in range(-1, -len(string) - 1, -1)]))

    
            