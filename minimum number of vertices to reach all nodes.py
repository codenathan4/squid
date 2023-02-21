class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seta = set()
        out = []
        for i in edges:
            seta.add(i[1])
        for i in range(n):
            if i not in seta:
                out.append(i)
        return out
