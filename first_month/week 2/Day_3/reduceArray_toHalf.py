from typing import Counter,List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr) // 2
        
        areEqual = all(ele == arr[0] for ele in arr)   # check if the array contains same elements
        if areEqual:
            return 1
        elif(len(arr) == len(counter)):
            return n
        
        size = set()
        i = 0
        while i < n:
            most_frequent = max(counter, key=counter.get)
            i += counter[most_frequent]
            counter[most_frequent] = 0
            size.add(most_frequent)

                
        return len(size)


s = Solution()
print(s.minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))