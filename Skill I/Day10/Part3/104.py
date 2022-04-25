# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        compareList = []
        if root is not None:
            compareList.append((1, root))
        depth = 0
        
        
        while compareList != []:
            currentDepth, root = compareList.pop() 
            if root is not None:
                depth = max(depth, currentDepth) 
                compareList.append((currentDepth+1, root.left))
                compareList.append((currentDepth+1, root.right))
        return depth

