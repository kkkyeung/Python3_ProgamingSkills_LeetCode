def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Solution from discuss, using 2 head to find , slow and fast.
# when fast arrives at the end, the slow will be in the middle
# then just return the slow