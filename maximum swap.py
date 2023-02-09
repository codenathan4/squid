class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 11:
            return num
        n = [int(x) for x in str(num)]
        m = sorted(n,reverse=True)
        for i in range(len(n)):
            if n[i] != m[i]:
                for j in range(len(n)-1,-1,-1):
                    if n[j] == m[i]:
                        n[i],n[j]=n[j],n[i]
                        break                    
                break       
                
        return int(''.join(str(x) for x in n))
