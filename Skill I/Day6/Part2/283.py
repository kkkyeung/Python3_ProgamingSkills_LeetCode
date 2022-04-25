class Solution:
    def moveZeroes(self, nums: list) -> None:
        Iamzero = 0
        for NotZero in range(len(nums)):
            if nums[NotZero] != 0 and nums[Iamzero] == 0:
                nums[Iamzero], nums[NotZero] = nums[NotZero], nums[Iamzero]

                
            if nums[Iamzero] != 0:
                Iamzero += 1