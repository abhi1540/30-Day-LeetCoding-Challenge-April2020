class Solution:
    
    leftheight = 0
    rightheight = 0
    longest_len = float('-inf')
    leftdia = 0
    rightdia = 0
    maxdia = 0

    
    def PathSum(self, root):
        
        if root is None:
            return 0
        
        left = max(0, self.PathSum(root.left))
        right = max(0, self.PathSum(root.right))
        self.longest_len = max(self.longest_len, left + right + root.val)  
        return max(left, right)  + root.val
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        self.PathSum(root)
        return self.longest_len