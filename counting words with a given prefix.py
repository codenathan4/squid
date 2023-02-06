class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        out = 0
        for i in words:
            if len(pref) <= len(i) and i[:len(pref)] == pref:
                out += 1
                
        return out
