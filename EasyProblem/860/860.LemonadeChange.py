class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = [],[]
        for i in range(len(bills)):
            if bills[i] == 5:
                five.append(5)
                continue
            if bills[i] == 10:
                ten.append(10)
                if len(five) >= 1:
                    five.remove(5)
                    continue
                else:
                    return False                
            if bills[i] == 20:
                if len(five) >= 1 and len(ten) >= 1:
                    five.remove(5)
                    ten.remove(10)
                    continue
                elif len(five) >= 3:
                    five.remove(5)
                    five.remove(5)
                    five.remove(5)
                    continue
                else:
                    return False
        return True

# Runtime: 1984 ms, faster than 5.03% of Python3 online submissions for Lemonade Change.
# Memory Usage: 17.6 MB, less than 97.16% of Python3 online submissions for Lemonade Change.