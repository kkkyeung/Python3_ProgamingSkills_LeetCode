class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        #print(s)
        #print(t)
        
        if len(s) == 0:
            return t
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return t[i]
            return t[len(t) - 1]

# Fast Solution in Discuss:
# def findTheDifference(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """
#     ans = 0
#     for c in s + t:
#         ans ^= ord(c)
#     return chr(ans)