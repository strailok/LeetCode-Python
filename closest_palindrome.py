class Solution:
    def nearestPalindromic(self, n: str) -> str:
        i = 1
        num = int(n)
        closest = 0
        while True:
            if self.isPalindrome(num-i):
                closest = num-i
                break
            if self.isPalindrome(num+i):
                closest = num+i
                break
            i += 1
        return str(closest)
    
    def isPalindrome(self,n):
        a = str(n)
        if a[0:] == a[::-1]:
            return True
        return False
