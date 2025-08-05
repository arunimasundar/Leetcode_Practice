# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=[]
        for char in s:
            if char.isalnum():
                l.append(char.lower())
        revl=l[::-1]

        if l==revl:
            return True
        else:
            return False