
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rec = {}
        out = 0
        for i in time:
            if (60-i%60)%60 in rec:
                out += rec[(60 - i%60)%60]
            if i%60 in rec:
                rec[i%60] += 1
            else:
                rec[i%60] = 1
        
        return out
