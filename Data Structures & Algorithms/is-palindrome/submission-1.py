class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        if not s:
            return True
        for ch in s:
            if ch.isalnum():
                arr.append(ch)
        op = "".join(arr)

        if op.lower() == op[::-1].lower():
            return True
        return False
        