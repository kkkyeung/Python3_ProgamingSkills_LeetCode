class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        if len(salary) == 1:
            return sum(salary)
        else:
            return sum(salary) / len(salary)