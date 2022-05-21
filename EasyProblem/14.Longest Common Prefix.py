class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        for i, ch in enumerate(min(strs,key=len)):
            for other in strs:
                if other[i] != ch:
                    return min(strs,key=len)[:i]
        return min(strs,key=len) 