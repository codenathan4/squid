class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = sum(int(i) for i in s)
        zeroes = len(s) - ones
        if zeroes == len(s) or zeroes == 0:
            return 0
        previousOnes = 0
        previousZeroes = 0
        count = 0
        for i in s:
            if i == '0':
                count += previousOnes*(ones-previousOnes)
                previousZeroes += 1 
            else:
                count += previousZeroes*(zeroes-previousZeroes)
                previousOnes += 1 
        return count
