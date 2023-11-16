# Time: O(n)
# Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, curr = 1, 2
        for _ in range (2, n):
            temp = curr # 储存前面的那个
            curr = curr + prev # 计算当前的
            prev = temp # 计算下一个（最后一次用不到）
        
        return curr