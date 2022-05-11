class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = 0
        for i in range(len(s[::-1])):
            if s[::-1][i].isalpha():
                output += 1
            elif output > 0:
            # or just elif output:
                break
        return output

# Runtime: 41 ms, faster than 51.53% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 80.39% of Python3 online submissions for Length of Last Word.