#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

IS_LEFT = False
NODES = []
def getInOrder(tree, node):
    # if node == -1:
    #     return
    
    if tree[node][1] != -1:
        global IS_LEFT
        IS_LEFT = tree[node][0] <= tree[tree[node][1]][0]
        getInOrder(tree, tree[node][1])
    
    NODES.append((tree[node][0], IS_LEFT))
    IS_LEFT = False

    if tree[node][2] != -1:
        getInOrder(tree, tree[node][2])


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    getInOrder(tree, 0)

    for i in range(len(NODES) - 1):
        if NODES[i][1]:
            return False
        
        if NODES[i][0] > NODES[i + 1][0]:
            return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = [0] * nodes
    for i in range(nodes):
        tree[i] = tuple(map(int, sys.stdin.readline().strip().split()))

    if nodes in {0, 1}:
        print("CORRECT")
    else:
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()