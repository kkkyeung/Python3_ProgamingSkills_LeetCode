# https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/148877/Python-5-lines-BFS-solution


class Solution(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
