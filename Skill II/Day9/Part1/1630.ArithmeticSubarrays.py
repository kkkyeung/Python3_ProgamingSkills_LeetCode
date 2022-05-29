class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            a = nums[l[i]:r[i]+1]
            a.sort()
            output.append(all(a[i - 2] - a[i - 1] == a[i - 1] - a[i] for i in range(2, len(a))))
        return output


# Upgrade Question based on Skill I Day4 Part2

#Runtime: 215 ms, faster than 77.00% of Python3 online submissions for Arithmetic Subarrays.
# Memory Usage: 14.1 MB, less than 90.92% of Python3 online submissions for Arithmetic Subarrays.