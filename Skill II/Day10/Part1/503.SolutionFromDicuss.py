class Solution:
    def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        for i in range(len(A)) * 2:
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res

# https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice