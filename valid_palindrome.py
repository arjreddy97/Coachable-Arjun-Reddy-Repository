class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(left+1,right,s) or self.is_palindrome(left,right-1,s)
            else:
                left += 1
                right -=1
        return True


    def is_palindrome(self,left,right,string):
        
        while left < right:
            if string[left] != string[right]:
                return False

            left += 1
            right -=1

        return True
    

    
