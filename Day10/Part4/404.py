class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        DepthList = [(root, False)]
        LeftTotal = 0
        
        while DepthList:
            currentDepth, leftLeaf = DepthList.pop()
            if not currentDepth:
                continue
            if not currentDepth.left and not currentDepth.right:
                if leftLeaf:
                    LeftTotal += currentDepth.val
            else:
                DepthList.append((currentDepth.left, True))
                DepthList.append((currentDepth.right, False))
        return LeftTotal