# python3
import sys


def build_suffix_tree(text):
            
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
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
                        tree[new_node][text[j]] = (j, length - j, node)
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

                

            
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))