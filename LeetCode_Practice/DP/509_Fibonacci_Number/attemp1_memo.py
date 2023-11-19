class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n <= 1:
            return n
        
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)

        return memo[n]