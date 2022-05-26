class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        for i in s:
            if i in ['(','[','{']:
                output.append(i)
            else:
                if not output or {')':'(',']':'[','}':'{'}[i]!=output[-1]:
                    return False
                output.pop()
        return not output