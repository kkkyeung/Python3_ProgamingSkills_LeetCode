class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
                continue
            if bills[i] == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                    continue
                else:
                    return False                
            if bills[i] == 20:
                if five >= 1 and ten >= 1:
                    five -=1
                    ten -=1
                    continue
                elif five >= 3:
                    five -= 3
                    continue
                else:
                    return False
        return True

# Runtime: 1323 ms, faster than 19.72% of Python3 online submissions for Lemonade Change.
#  Memory Usage: 18.1 MB, less than 21.27% of Python3 online submissions for Lemonade Change.