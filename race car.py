class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque([(0,1)])
        out = 0
        
        while q:
            l = len(q)
            while l>0:
                p, s = q.popleft()

                if p == target:
                    return out

                q.append((p+s,s*2))

                if (p+s > target and s > 0) or (p+s < target and s < 0):
                    q.append((p,-1 if s>0 else 1))
                
                l -= 1
            
            out += 1
            
        return out
