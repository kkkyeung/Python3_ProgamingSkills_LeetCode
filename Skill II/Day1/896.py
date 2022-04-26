class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        num = True
        if nums[0] > nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    num = True
                elif nums[i] == nums[i+1]:
                    continue
                else:
                    num = False
                    break
            return num
        elif nums[0] < nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    num = True
                elif nums[i] == nums[i+1]:
                    continue
                else:
                    num = False
                    break
            return num
        elif len(set(nums)) == 1:
            return True
        else:
            return False





# Runtime: 1000 ms, faster than 93.87% of Python3 online submissions for Monotonic Array.
# Memory Usage: 28 MB, less than 61.80% of Python3 online submissions for Monotonic Array.