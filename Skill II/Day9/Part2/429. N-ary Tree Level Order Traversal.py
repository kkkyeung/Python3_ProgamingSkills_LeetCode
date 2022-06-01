"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution: 
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level):
            if root == None: return
            if level == len(output):
                output.append([])
            output[level].append(root.val)
            for child in root.children:
                dfs(child, level + 1)
              
        output = []
        dfs(root, 0)
        return output


#dfs method
# Runtime: 84 ms, faster than 29.22% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 16 MB, less than 51.73% of Python3 online submissions for N-ary Tree Level Order Traversal.