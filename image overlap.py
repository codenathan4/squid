class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a=[]
        b=[]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    a.append((i,j))
                if B[i][j]:
                    b.append((i,j))
        dic={}
        for ax,ay in a:
            for bx,by in b:
                if (ax-bx,ay-by) not in dic:
                    dic[(ax-bx,ay-by)]=1
                else:
                    dic[(ax-bx,ay-by)]+=1
        return max(dic.values()) if dic else 0
