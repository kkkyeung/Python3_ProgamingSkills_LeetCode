class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if((target - nums[i]) in nums and nums.index(target - nums[i]) != i):
                return [i, nums.index(target - nums[i])]


# Runtime: 944 ms, faster than 33.50% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 76.32% of Python3 online submissions for Two Sum.