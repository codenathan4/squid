class DetectSquares:

    def __init__(self):
        self.points = collections.Counter()

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x,y)] += 1 

    def count(self, point: List[int]) -> int:
        
        xo, yo = point[0], point[1]

        out = 0 

        for k, v in self.points.items():
            dx, dy = abs(k[0] - xo), abs(k[1] - yo)
            if dx != dy or (dx == 0 and dy == 0): 
                continue 
            
            if (k[0],yo) in self.points and (xo, k[1]) in self.points: 
                out += v * self.points[(k[0],yo)] * self.points[(xo,k[1])]
        
        return out
