class Solution:
    def sumOddLengthSubarrays(self, A):
        output = 0
        for i in range(1, len(A) + 1, 2):
            for j in range(len(A) - i + 1):
                output += sum(A[j:j + i])
        return output