class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        print(s)
        print(t)
        
        if len(s) == 0:
            return t
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return t[i]
            return t[len(t) - 1]