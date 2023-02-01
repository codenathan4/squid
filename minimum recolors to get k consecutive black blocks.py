class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 1
        r = k
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        out = w
        
        while r < len(blocks):
            if blocks[r] != blocks[l-1]:
                if blocks[r] == 'W':
                    w += 1
                else:
                    w -= 1    
            out = min(out,w)
            r += 1
            l += 1
        
        return out
