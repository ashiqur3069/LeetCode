class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        stack.append(asteroids[0])

        for i in asteroids[1:]:
            while stack and i < 0 < stack[-1]:
                if stack[-1] < abs(i):
                    stack.pop()
                    continue
                elif stack[-1] == abs(i):
                    stack.pop()
                break
            else:
                stack.append(i)

        return stack
