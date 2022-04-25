class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head: 
            # print(ans*2)
            # print(head.val)
            ans = 2*ans + head.val
            head = head.next 
        return ans 