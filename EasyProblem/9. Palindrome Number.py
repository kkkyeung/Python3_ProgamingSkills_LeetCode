class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

# Runtime: 75 ms, faster than 66.29% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 60.46% of Python3 online submissions for Palindrome Number.