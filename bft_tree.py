# Breadth First Traversal of a tree
"""
            Tree
            1
           / \
         /    \
        2      3
       / \
     /    \
    4      5
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

    def add_children(self, node1, node2):
        self.left = node1
        self.right = node2


def height(node):
    if node is None:
        return 0
    l_height = height(node.left)
    r_height = height(node.right)
    if l_height > r_height:
        return l_height + 1
    else:
        return r_height + 1


def printCurrentLevel(root, level):
    if root is None:
        return
    if not level:
        print(root.data, end=" ")
    else:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


def printLevelOrder(root):
    h = height(root)
    print(f"Height of the tree = {h-1}")
    print("Level order traversal of the binary tree is ")
    for i in range(0, h+1):
        printCurrentLevel(root, i)


if __name__ == "__main__":
    tree = Node(1)
    tree.add_children(Node(2), Node(3))
    tree.left.add_children(Node(4), Node(5))
    # tree.right.add_children(Node(6), Node(7))
    # tree.right.left.add_children(Node(8), Node(9))
    printLevelOrder(tree)
