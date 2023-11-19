class Solution:
    def climbStairs_tabulation(self, n: int) -> int:
        pass

    def climbStairs_memo(self, n: int) -> int:
        pass

num_staris = int(input("Please input the number of stairs: "))
sol = Solution()

ways = str(sol.climbStairs_memo(num_staris))
print(ways + " ways")
