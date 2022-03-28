class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0  
        left = 0
        
        for right in range(len(s)):
            curr = s[right]
            if curr in count:             # count[curr] = 1 + count.get(curr,0) -> shortcut
                count[curr] += 1
            else:
                count[curr] = 1
                
            mostFrequent = max(count.values())
            currWindow = right - left + 1
            if currWindow - mostFrequent > k:
                count[s[left]] -= 1
                left += 1
                currWindow = right - left + 1
                
            res = max(res, currWindow)
            
        return res