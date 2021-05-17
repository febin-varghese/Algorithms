"""
Depth First Search traversal of a tree
3 methods
1. Inorder: (left, root, right)
2. Preorder: (root, left, right)
3. Postorder: (left, right, root)
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


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


def printPreorder(root):
    if root:
        print(root.data, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    tree = Node(1)
    tree.add_children(Node(2), Node(3))
    tree.left.add_children(Node(4), Node(5))
    print("Inorder traversal of binary tree")
    printInorder(tree)
    print("\nPreorder traversal of binary tree")
    printPreorder(tree)
    print("\nInorder traversal of binary tree")
    printPostorder(tree)
