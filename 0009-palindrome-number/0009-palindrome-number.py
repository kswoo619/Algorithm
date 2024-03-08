class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        for i in range(len(x) // 2 + 1):
            if x[i] != x[-(i+1)]:
                return False
        
        return True
