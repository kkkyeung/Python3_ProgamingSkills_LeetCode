class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.help(root) != -1
        
    def help(self, root):
        if not root:
            return 0
        left = self.help(root.left)
        if left == -1:  
            return -1
        right = self.help(root.right)
        if right == -1: 
            return -1
        
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

