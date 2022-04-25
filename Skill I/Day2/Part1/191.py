class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        print(bin(n))
        return str(bin(n)).count("1")