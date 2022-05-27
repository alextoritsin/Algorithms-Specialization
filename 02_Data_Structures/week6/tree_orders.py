# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = [] 
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def getInOrder(index):
        
            if self.left[index] != -1:
                getInOrder(self.left[index])

            self.result.append(self.key[index])

            if self.right[index] != -1:
                getInOrder(self.right[index])

        getInOrder(0)

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def getPreOrder(index):
            self.result.append(self.key[index])
            
            if self.left[index] != -1:
                getPreOrder(self.left[index])

            if self.right[index] != -1:
                getPreOrder(self.right[index])

        getPreOrder(0)
                    
        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def getPostOrder(index):
        
            if self.left[index] != -1:
                getPostOrder(self.left[index])

            if self.right[index] != -1:
                getPostOrder(self.right[index])

            self.result.append(self.key[index])

        getPostOrder(0)
                    
        return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()