class Solution:
    def __init__(self, w: List[int]):
        self.l = []
        self.wt = 0
        
        for i in w:
            self.wt += i
            self.l.append(self.wt)

    def pickIndex(self) -> int:
        return bisect.bisect(self.l, random.randrange(self.wt))
