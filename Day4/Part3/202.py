class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                # example n = 19  ,  divmod(n,10) = divmod(19, 10) ,
                # then the divisor of 19 / 10 will be 1 (n), and remainder will be 9 (digit) which is (n, digit) on the left hand side.
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            # For example, for the first loop we get the total_sum is 9**2 = 81 and the second loop n is 1, so 1/10 = 0,1.
            # thus we know the digit in this case is becoming 1 and we can add 81 to combine the total sum to 82.
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            print(seen)
            seen.add(n)
            n = get_next(n)
        return n == 1