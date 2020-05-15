class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        INT_MIN = float("-infinity") 
        INT_MAX = float("infinity") 
        
        n = len(preorder)
        if n == 0:
            return null
        
        root = TreeNode(preorder[0])
        if n == 1:
            return root
        
        self.const_bst(preorder, n, 1, root, INT_MAX, INT_MIN)
        return root
        
        
    def const_bst(self, preorder, n, curr, root, maxval, minval):
        
        if curr == n or preorder[curr] > maxval  or preorder[curr] < minval:
            return curr
        
        if preorder[curr] < root.val:
            root.left = TreeNode(preorder[curr])
            curr += 1
            curr = self.const_bst(preorder, n, curr, root.left, root.val-1, minval)
            
            
        if curr == n or preorder[curr] > maxval  or preorder[curr] < minval:
            return curr
        
        root.right = TreeNode(preorder[curr])
        curr += 1
        curr = self.const_bst(preorder, n, curr, root.right, maxval, root.val + 1)
        return curr
 