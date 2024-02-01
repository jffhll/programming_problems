import sys

from Tree import Tree

def main():
    tree = Tree(5)
    tree.traverseFromRoot()
    tree.addNode(tree.getRoot(), 3)
    tree.traverseFromRoot()
    tree.addNode(tree.getRoot(), 8)
    tree.addNode(tree.getRoot(), 4)
    tree.addNode(tree.getRoot(), 10)
    tree.traverseFromRoot()
    tree.addNode(tree.getRoot(), 1)
    tree.addNode(tree.getRoot(), 9)
    tree.addNode(tree.getRoot(), 1)
    tree.addNode(tree.getRoot(), 9)
    tree.addNode(tree.getRoot(), 2)
    tree.addNode(tree.getRoot(), 1000)
    tree.traverseFromRoot()


if __name__ == "__main__":
    main()
