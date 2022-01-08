class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        if n == 1:
            return True
        elif n == 3 :
            return True
        elif n % 3 :
            return False
        elif 1 < n < 3:
            return False
        
        return self.isPowerOfThree(n//3)