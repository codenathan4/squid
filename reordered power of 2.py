class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        for i in range(30):
            if s == sorted(str(pow(2,i))):
                return True
        return False
