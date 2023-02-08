class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:       
        d = defaultdict(set)
        for n in adjacentPairs:
            d[n[0]].add(n[1])
            d[n[1]].add(n[0])
        
        ans = []
        for key,value in d.items():
            if len(value) == 1:
                val = value.pop()
                ans.extend([key,val])
                d[val].remove(key)
                d.pop(key)
                if not d[val]: d.pop(val)
                break
        while d:
            temp = ans[-1] 
            val = d.pop(temp).pop()
            ans.append(val)
            d[val].remove(temp)
            if not d[val]: d.pop(val)
        return ans
