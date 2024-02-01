from Node import Node

class Tree:
    def __init__(self, rootValue):
        self.root = Node(rootValue)

    def getRoot(self) -> Node:
        return self.root

    def addNode(self, cur: Node, val: int) -> Node:
        if val <= cur.getVal():
            if cur.left is None:
                cur.left = Node(val)
            else:
                self.addNode(cur.left, val)
        else:
            if cur.right is None:
                cur.right = Node(val)
            else:
                self.addNode(cur.right, val)

    def traverseFromRoot(self):
        self.traverse(self.root)
        print()
    
    def traverse(self, cur: Node) -> None:
        if cur.left is not None:
            self.traverse(cur.left)

        cur.printNode()

        if cur.right is not None:
            self.traverse(cur.right)
