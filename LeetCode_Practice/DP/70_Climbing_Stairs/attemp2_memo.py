# top - down 自上而下

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict) -> int:
        if n <= 2:
            return n
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        
        return memo[n]
    
num_staris = int(input("Please input the number of stairs: "))
sol = Solution()

ways = str(sol.climbStairs(num_staris))
print(ways + " ways")

