class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev, curr = 0, 1
        for _ in range(1, n):
            temp = curr
            curr = curr + prev
            prev = temp

        return curr