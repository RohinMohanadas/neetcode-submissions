class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aster = []
        for i in asteroids:
            while aster and i < 0 and aster[-1] > 0: # collision
                if abs(i) > abs(aster[-1]):
                    aster.pop()
                elif abs(i) < abs(aster[-1]):
                    i = 0
                else:
                    i = 0
                    aster.pop()
            if i:
                aster.append(i)

        return aster 
        