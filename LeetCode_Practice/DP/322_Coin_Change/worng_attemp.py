class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        count = 0
        coins.sort(reverse = True)
        for i in range(len(coins)):
            num = amount // coins[i]
            count += num
            amount -= coins[i] * num
        
        if amount != 0:
            return -1
        else:
            return count
        
# [186,419,83,408] 失败，贪心不能完美解决问题