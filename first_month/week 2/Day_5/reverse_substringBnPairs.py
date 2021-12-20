class Solution:
    def reverseParentheses(self, s: str) -> str:
        list1=[]
        list1[:0]=s
        n = len(list1)
        s1 = []
        s2 = []
     
        for i in range(0,n):
            if(list1[i] != ')'):
                s2.append(list1[i])
            else:
                b = len(s2) - 1
                for t in range(b,-1,-1):
                    if(s2[t] != '(' ):
                        s1.append(s2.pop())
                    else:
                        s2[t:] = s1[:]
                    
                        s1 = []
                        break
        return "".join(s2)


s = Solution()
print(s.reverseParentheses("(u(love)i)"))