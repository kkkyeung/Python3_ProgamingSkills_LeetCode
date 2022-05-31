#review and add the new solution

def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for times in range(4):
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j] # swap(mat[i][j],mat[j][i])
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j] #swap(mat[i][j], mat[i][n-1-j])
            if(mat == target):
                return True
        return False