class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                output.append(nums[i+1])
                continue
            elif nums[i+1] == nums[i]:
                newNumList = nums[i:]
                for j in range(len(newNumList)):
                    if not newNumList[j] > nums[i]:
                        continue
                    elif j == len(newNumList) -1 and not newNumList[j] > nums[i]:
                        output.append(-1)
                    else:
                        output.append(newNumList[j])
                        break
            else:
                output.append(-1)
                
                
        if nums[len(nums)-1] > nums[len(nums)-2]:
            output.append(-1)
        else:
            output.append(nums[len(nums)-2])
        
        return output

# unfinished