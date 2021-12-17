from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        
        while k > 0:
            most_frequent = max(counter, key=counter.get)  # to find the key with max value in dictionary
            ans.append(most_frequent)
            counter[most_frequent] = 0
            k -= 1
        return ans


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))
print(s.topKFrequent([1],1))


        