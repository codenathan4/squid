class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid) - 1][len(grid) - 1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        d = [-1,0,1,0,-1,-1,1,1,-1]
        for i, j, count in q:
            if i == j == len(grid) - 1:
                return count
            k = 0;l=1
            for _ in range(8):
                if 0 <= i+d[k] < len(grid) and 0 <= j+d[l] < len(grid) and not grid[i+d[k]][j+d[l]]:
                    grid[i+d[k]][j+d[l]] = 1
                    q.append((i+d[k], j+d[l], count + 1))
                k +=1; l+=1    
        return -1
