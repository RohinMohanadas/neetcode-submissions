class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            a = defaultdict(int)
            b = defaultdict(int)
            for i,j in zip(s,t):
                a[i] +=1
                b[j] +=1
            if a == b:
                return True
            else:
                return False