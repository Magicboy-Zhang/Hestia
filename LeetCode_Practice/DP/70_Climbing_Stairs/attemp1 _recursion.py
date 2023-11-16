# recursion - slow - O(2^n)

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        complex
        '''
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        '''
        simple
        '''
        if n <= 2:
            return n
    
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
num_stairs = int(input("Please input the number of stairs: "))

sol = Solution()
ways = str(sol.climbStairs(num_stairs))

print(ways + " ways")



