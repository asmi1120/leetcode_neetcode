class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            while stack and asteroids[i]<0 and stack[-1]<-asteroids[i] and stack[-1]>0:
                stack.pop()
            if stack and asteroids[i]<0 and stack[-1]>0:
                if -asteroids[i]==stack[-1]:
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack
                


        