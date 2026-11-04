class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        reversed_text = text[::-1]
        return text == reversed_text
        
