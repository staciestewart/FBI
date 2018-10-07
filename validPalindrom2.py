# Given a non-empty string s, 
# you may delete at most one character.
# Judge whether you can make it a palindrome.


class Solution:
    def validPalindrome(self, s):
    
        
        # Define palindrom checking function
        def is_pali_range(i, j):
            
            # If all mirror character is the same then return True
            return all(s[k] == s[j-k+i] for k in range(i, j))
        
        # Divide the string by half and iterate over the range
        for i in range(int(len(s) / 2)):
            
            # If the mirroring character is not the same
            if s[i] != s[~i]:
                
                # remove on character from end or beginning and check for palindrome
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
            
        return True