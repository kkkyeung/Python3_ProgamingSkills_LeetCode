class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dStringsList = [str(d) for d in digits]
        dString = "".join(dStringsList)
        digit = int(dString)
        outputDigit = digit + 1
        output = [int(i) for i in str(outputDigit)]
        return output