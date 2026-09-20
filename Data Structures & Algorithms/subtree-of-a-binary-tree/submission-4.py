# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Self0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge case 
        if not subRoot: return True # None is alwasy subtree
        if not root: return False # if subroot is not None, then it is false 

        if self.sameTree(root, subRoot):
            return True 
        else: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    


    def sameTree(self, q: Optional[TreeNode], p: Optional[TreeNode])-> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(q.left, p.left) and self.sameTree(q.right, p.right)
        else:
            return False
        