class Solution:
    def romanToInt(self, s: str) -> int:
        rec = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000 }
        out = rec[s[len(s)-1]]

        for i in range(len(s)-2,-1,-1):       
            if rec[s[i]]  >= rec[s[i + 1]]:
                out += rec[s[i]] 
            else:
                out -= rec[s[i]] 

        return out
