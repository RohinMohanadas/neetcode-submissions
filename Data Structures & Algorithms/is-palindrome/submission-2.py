class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        s = s.lower()
        print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"), ord("9"))
        def alnum(char: str) -> bool:
            if (char[0] >= "A" and char[0]<="Z") or (char[0] >="a" and char[0] <="z") or            (char[0] >="0" and char[0] <="9"):
                return True
            return False
             
        while start < end:
            print(s[start], s[end])
            if not alnum(s[start]):
                start +=1
                continue
            if not alnum(s[end]):
                end -=1
                continue
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1

        return True
        