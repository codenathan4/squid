class Solution:
    def minOperations(self, logs: List[str]) -> int:
        d = 0
        for i in logs:
            if i[:-1] == '..':
                if d: d -= 1
            elif i[:-1] != '.':
                d += 1
        
        return d
