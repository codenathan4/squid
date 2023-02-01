class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        pfxsum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                pfxsum[i+1][j+1] = mat[i][j] + pfxsum[i+1][j] + pfxsum[i][j+1] - pfxsum[i][j]
        
        for i in range(m):
            for j in range(n):
                top=i-k if i-k>=0 else 0
                bot=i+k+1 if i+k+1<m+1 else m
                lef=j-k if j-k>=0 else 0
                rig=j+k+1 if j+k+1<n+1 else n
                mat[i][j] = pfxsum[bot][rig] + pfxsum[top][lef] - pfxsum[top][rig] - pfxsum[bot][lef]
        return mat
