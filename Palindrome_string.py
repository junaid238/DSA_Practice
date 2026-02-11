# this approach works in python only 
# python strings support reversing and converting numbers to strings 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_str_x = str_x[::-1]
        if str_x == rev_str_x:
            return True
        else:
            return False