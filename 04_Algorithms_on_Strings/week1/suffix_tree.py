# python3
import sys


def build_suffix_tree(text):

    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    tree = {0:{}}
    new_node = 0
    for i in range(len(text)):
        cur_node = 0
        for j in range(i, len(text)):
            char = text[i]
            if char in tree[cur_node]:
                pass
            else:
                new_node += 1
                tree[cur_node][char] = (i, j + 1, new_node)
                tree[new_node] = dict()
                if i < len(text) - 1:
                    new_node += 1
                    cur_node = tree[cur_node][char][2]
                    tree[cur_node][text[i + 1]] = (i + 1, len(text) - 1, new_node)
            


    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))