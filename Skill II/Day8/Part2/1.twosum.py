class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            if((target - nums[i]) in nums and nums.index(target - nums[i]) != i):
                output.append(i)
                output.append(nums.index(target - nums[i]))
                break
            else:
                continue
        return output