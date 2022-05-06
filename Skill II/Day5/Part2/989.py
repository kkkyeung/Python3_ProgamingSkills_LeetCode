class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numStr = ""
        output = []
        for i in range(len(num)):
            numStr += str(num[i])
        numInt = int(numStr)
        outputNum = numInt + k
        outputStr = str(outputNum)
        for i in range(len(outputStr)):
            output.append(outputStr[i])
        return output


# Runtime: 549 ms, faster than 22.87% of Python3 online submissions for Add to Array-Form of Integer.
# Memory Usage: 14.5 MB, less than 97.11% of Python3 online submissions for Add to Array-Form of Integer.