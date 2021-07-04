# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        node = root
        height = []
        level = 1
        
        def search(node, level):
            if node.left != None:
                search(node.left, level+1)
            if node.right != None:
                search(node.right, level+1)
            if node.left == None and node.right == None:
                height.append(level)
                return level
        
        search(node, 1)
        return max(height)
