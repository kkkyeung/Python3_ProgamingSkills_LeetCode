class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        alist = []
        for i in range(len(str(n))):
            alist.append(str(n)[i])
        return reduce(operator.mul, list(map(int, alist))) - sum(list(map(int, alist)))