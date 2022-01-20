class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k:
            return "0"
        
        res = ""
        s = []
        for i,v in enumerate(num):
            if not s:
                s.append(v)
            else:
                while k>0 and s and s[-1] > v:
                    k -= 1
                    s.pop()
                    
                s.append(v)
                
        while k > 0:
            k -= 1
            s.pop()
            
        if all(x == "0" for x in s):
            res = "0"
        else:
            res = ''.join(s)
            
        return res.lstrip('0') if res > "0" else res