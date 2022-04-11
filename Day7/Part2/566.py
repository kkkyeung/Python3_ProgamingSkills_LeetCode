class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        newmat = sum(mat,[])
        output = []
        columnSize = []
        if r * c != len(newmat):
            return mat
        for i in range(len(newmat)):
            columnSize.append(newmat[i])
            if len(columnSize) == c:
                #print("1 output:" + str(result))
                output.append(columnSize)
                columnSize = []
                #print("2 output:" + str(result))
                #print("3 output:" + str(output))
        return output