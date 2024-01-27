


class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val 
    def printTree(self):
        print(self.val)
    
    def inset(self, newVal):
        if self.val:
            if self.left is None:
                self.left = Node(newVal)
            if self.right is None:
                self.right = Node(newVal)
         
root = Node(10)
root.printTree()