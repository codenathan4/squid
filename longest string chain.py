class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        rec = {}
        out = 0
        
        for i in sorted(words,key=len):
            rec[i] = 1
            
            for j in range(len(i)):
                h = i[:j] + i[j+1:]
                
                if h in rec:
                    rec[i] = max(rec[h] + 1,rec[i])
            
            out = max(out,rec[i])
        return out
