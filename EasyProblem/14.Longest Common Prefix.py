class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        for i, ch in enumerate(min(strs,key=len)):
            for all in strs:
                if all[i] != ch:
                    return min(strs,key=len)[:i]
        return min(strs,key=len)

# do the comparation between the shortest string and all otherstring using index.