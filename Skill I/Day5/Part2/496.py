class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        outputlist = []
        a = nums2[:]
        for i in range(len(nums1)):
            position = a.index(nums1[i])
            if position == len(a) - 1:
                print("output1")
                outputlist.append(-1)
            else:
                del a[0:position+1]
                x = [i for i in a if i>nums2[position]]
                if len(x) >= 1:
                    print("output3")
                    outputlist.append(x[0])
                else:
                    outputlist.append(-1)
                a = nums2[:]
        return outputlist