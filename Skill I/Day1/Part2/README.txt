Concept:

Remove the highest salary and lowest salary of the list, then based on the len of the list to find the avag salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        if len(salary) == 1:
            return sum(salary)
        else:
            return sum(salary) / len(salary)



One line:
(sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)