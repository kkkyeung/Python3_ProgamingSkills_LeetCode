class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if needle not in haystack:
                return -1
            elif needle is None:
                return 0
            else:
                return haystack.find(needle)

#Runtime: 35 ms, faster than 81.96% of Python3 online submissions for Implement strStr().
#Memory Usage: 13.8 MB, less than 85.73% of Python3 online submissions for Implement strStr().