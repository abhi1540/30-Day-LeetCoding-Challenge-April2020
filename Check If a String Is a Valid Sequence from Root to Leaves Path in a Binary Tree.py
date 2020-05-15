class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        currpos = 0
        return self.checkval(root, arr, currpos)
        
        
        
    def checkval(self, root, arr, currpos):
        
        if root is None:
            return False
        
        if currpos == len(arr):
            return False
        
        if root.val == arr[currpos] and (currpos == len(arr) - 1) and root.left is None and root.right is None:
            
            return True
        if currpos < len(arr) and root.val == arr[currpos]:
            return self.checkval(root.left, arr, currpos + 1) or self.checkval(root.right, arr, currpos + 1)