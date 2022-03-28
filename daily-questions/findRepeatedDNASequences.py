from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeatedSequences = {}
        result = []
        start = 0
        
        for start in range(len(s)-9):
            currSubString = s[start : start+10]
            repeatedSequences[currSubString] = 1 + repeatedSequences.get(currSubString,0)
            
            if repeatedSequences[currSubString] == 2:
                result.append(currSubString)
    
        return result
                


s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))