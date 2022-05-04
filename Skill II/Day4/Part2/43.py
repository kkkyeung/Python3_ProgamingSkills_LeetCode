class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        i_num1 = i_num2 = 0
        for p in range(len(num1)):
            i_num1 = i_num1 + digits[num1[p]] * pow(10, len(num1)-p-1)
        for p in range(len(num2)):
            i_num2 = i_num2 + digits[num2[p]] * pow(10, len(num2)-p-1)
        ans = str(i_num1 * i_num2)
        return ans