# bottom - up 自下而上
# Time & Space: O(n) & O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        # 创建一个长度为n的列表，并填充base cases
        '''
        complex
        '''
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2

        '''
        simple
        '''
        dp = [1, 2] + [0] * (n - 2)

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]
    
num_stairs = int(input("Please input the number of stairs: "))
sol = Solution()

ways = str(sol.climbStairs(num_stairs))
print(ways + " ways")