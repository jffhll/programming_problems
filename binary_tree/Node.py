class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def printNode(self):
        print(self.data, end = " ")

    def getVal(self):
        return self.data
    
    def setVal(self, val):
        self.data = val