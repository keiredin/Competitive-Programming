from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        coins = 0
        cycle = n / 3
        for i in range(1,n,2):
            coins += piles[i]
            cycle -= 1
            if cycle == 0:
                return coins
                
s = Solution()
print(s.maxCoins([2,4,5]))
print(s.maxCoins([9,8,7,6,5,1,2,3,4]))
