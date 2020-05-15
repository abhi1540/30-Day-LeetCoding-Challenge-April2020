class Solution:
    
    leftheight = 0
    rightheight = 0
    longest_len = 0
    leftdia = 0
    rightdia = 0
    maxdia = 0

    def height(self,root):
        
        if root is None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))
        
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
         
        if root is None:
            return 0
        
        ## passes through root
        self.leftheight = self.height(root.left)
        self.rightheight = self.height(root.right)
        self.longest_len = max(self.longest_len, 1 + self.leftheight +  self.rightheight)
        
        ## not passes through root
        self.leftdia = self.diameterOfBinaryTree(root.left)
        self.rightdia = self.diameterOfBinaryTree(root.right)
        self.maxdia = max(self.leftdia, self.rightdia)
        
        return max(self.longest_len, self.maxdia) - 1