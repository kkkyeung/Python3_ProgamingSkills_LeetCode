class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        :type str: str
        :rtype: bool
        """
        
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        print(ss.find(s))
        return ss.find(s) != -1