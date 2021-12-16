class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if(l%2 != 0):
            return False
        stack = []
        openingP = "({["
        closingP = ")}]"
        for parenthesis in s:
            if parenthesis in openingP:
                stack.append(parenthesis)
            elif parenthesis in closingP:
                if (stack):
                    op = stack[-1]
                    if(openingP.index(op) == closingP.index(parenthesis)):
                        stack.pop()
        return False if len(stack) else True  

s = Solution()
print(s.isValid("()[]{}"))