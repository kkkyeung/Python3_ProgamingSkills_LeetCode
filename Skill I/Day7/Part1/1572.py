class Solution:
    import math
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        for i in range(len(mat)):
            output += mat[i][i]
            print("this is 1 output:" + str(mat[i][i]))
            output += mat[len(mat)-1-i][i]
            print("this is 2 output:" + str(mat[len(mat)-1-i][i]))
            
        if len(mat) % 2 == 1:
            output -= mat[len(mat)//2][len(mat)//2]
        return output