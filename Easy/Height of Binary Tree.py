# Given the root of a binary tree, find the maximum depth of the tree.

# Note: The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if root is None:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1