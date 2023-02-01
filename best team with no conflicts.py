class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        rec = [0] * (max(ages) + 1)
        for s,a in sorted(zip(scores, ages)):
            rec[a] = s + max(rec[:a + 1])
        return max(rec)
