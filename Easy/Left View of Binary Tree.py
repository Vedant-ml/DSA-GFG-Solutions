# Given the root of a binary tree. Return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

# Note: If the tree is empty, return an empty list.

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self,root):
        result = []

        def preorder(node, level):
            if node is None:
                return

            # First node encountered at this level
            if level == len(result):
                result.append(node.data)

            preorder(node.left, level + 1)
            preorder(node.right, level + 1)

        preorder(root, 0)

        return result
        