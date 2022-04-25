class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
            
        DiffPosition = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                DiffPosition.append(1)
            else:
                DiffPosition.append(0)
        return sum(DiffPosition) == 2 or sum(DiffPosition) == 0