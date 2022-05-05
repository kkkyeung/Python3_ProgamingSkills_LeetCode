class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

# Runtime: 24 ms, faster than 99.34% of Python3 online submissions for Add Binary.
# Memory Usage: 13.9 MB, less than 25.52% of Python3 online submissions for Add Binary.


