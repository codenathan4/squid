class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = 0
        direction = 0
        
        for i in instructions:
            if i == 'L':
                position *= 1j
                direction += 1
            elif i == 'R':
                position *= -1j
                direction -= 1
            else:
                position += 1   
          
        if direction%4 != 0 or position == 0:
            return True
