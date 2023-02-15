class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def helper(n):
            if n%26:
                if n >26:
                    return helper(n//26) + [chr(n%26+64)]
                return [chr(n%26+64)]
            elif n == 26:
                return ['Z']
            else:
                return helper(n//26-1) + ['Z']
        return ''.join(helper(columnNumber))
