class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for i in range(len(nums)-2): #assume the len of list is 3, when we calculating nums[i] < nums[i + 1] + nums[i + 2] first time, so nums[0] < nums[0 + 1] + nums[0 + 2], and the nums[0 + 2] in here is meaning the third value of the list, so the loop range should be 1.
            print(i) 
            if nums[i] < nums[i + 1] + nums[i + 2]: # see line 4, and because we already sort the list to descending. and we already know nums[i] + nums[i + 1] > nums[i + 2] and nums[i] + nums[i + 2] > nums[i + 1], so we only need to find nums[i] < nums[i+1] + nums[i+2].
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0