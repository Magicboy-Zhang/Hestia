class Solution:
    def climbStairs_tabulation(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, curr = 1, 2
        for _ in range(2, n):
            temp = curr
            curr = curr + prev
            prev = temp
        
        return curr

    def climbStairs_memo(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n <= 2:
            return n
        
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)

        return memo[n]

num_staris = int(input("Please input the number of stairs: "))
sol = Solution()

ways = str(sol.climbStairs_memo(num_staris))
print(ways + " ways")
