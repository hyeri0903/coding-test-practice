# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traverse(root: TreeNode, answer):
            if root!=None:
                traverse(root.left, answer)
                answer.append(root.val)
                traverse(root.right, answer)
            
        answer = []
        traverse(root, answer)
        return answer
    
    
