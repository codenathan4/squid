class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = defaultdict(dict)
        for (u,v), cost in zip(equations, values):
            gr[u][v] = cost
            gr[v][u] = 1/cost
        def devide(Num,DeNum):
            if not(Num in gr and DeNum in gr):
                return -1
            q = [(Num,1)]
            vis = set()
            for Num, val in q:
                if Num == DeNum:
                    return val
                vis.add(Num)
                
                for i in gr[Num]:
                    if i not in vis:
                        q.append((i,val*gr[Num][i]))
                        
            return -1
        
        out = []
        for i in queries:
            out.append(devide(i[0],i[1]))
            
        return(out) 
