class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A

# Runtime: 350 ms, faster than 46.76% of Python online submissions for Add to Array-Form of Integer.
# Memory Usage: 13.9 MB, less than 57.18% of Python online submissions for Add to Array-Form of Integer.