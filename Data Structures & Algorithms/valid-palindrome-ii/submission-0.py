class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        counter1 = 0
        counter2 = 0
        
        option1 = True
        option2 = True
        while left < right:
            if s[left]!=s[right]:
                left+=1
                counter1 += 1
                continue
            left +=1
            right -=1

        left = 0
        right = len(s) - 1        


        while left < right:
            if s[left]!=s[right]:
                right-=1
                counter2 += 1
                continue
            left +=1
            right -=1
        
        if counter1 > 1 and counter2 > 1:
            return False
        else: 
            return True