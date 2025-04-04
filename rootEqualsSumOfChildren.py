# Definition of a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Check if the binary tree has a Root = Left + Right children

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if (root.left.val + root.right.val == root.val):
            return True
        else:
            return False    
