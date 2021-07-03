# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        tmp = []  #root -> leaf 까지의 합을 저장하는 임시 리스트
        
        if root == None:
            return False
        
        def sum_node(node, total, targetSum):
            if node.left != None:
                sum_node(node.left, total+node.left.val, targetSum)
            if node.right != None:
                sum_node(node.right, total + node.right.val, targetSum)
                
            if node.left == None and node.right == None:
                tmp.append(total)
                return total
        
        sum_node(root, root.val, targetSum)
        
        if targetSum in tmp:
            return True
        return False
