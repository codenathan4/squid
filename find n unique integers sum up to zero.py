class Solution:
    def sumZero(self, n: int) -> List[int]:
        neg = []
        pos = []
        for i in range(1,n//2+1):
            neg.append(-i)
            pos.append(i)
        
        return neg + ([0] if n%2 else []) + pos
