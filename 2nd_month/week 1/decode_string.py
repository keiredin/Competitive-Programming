class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        result = ""
        num = ""
        for i in s:
            if i != ']':
                stack1.append(i)
            else:
                result = ""
                # print(stack1)
                while stack1[-1] != '[':
                    result += stack1.pop()
                
                r = result[::-1]
                # print(r)
                stack1.pop()
                while stack1 and stack1[-1] in '0123456789':
                    num += stack1.pop()
                n =num[::-1]
                num = ""
                rep = int(n) * r
                for r in rep:
                    stack1.append(r)
                
        a = "".join(stack1)
        return a
