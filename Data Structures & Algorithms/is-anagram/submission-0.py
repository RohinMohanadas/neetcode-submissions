class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashOne = {}
        hashTwo = {}

        if len(s)!=len(t):
            return False
        else:
            for idx,char in enumerate(s):
                if char in hashOne:
                    hashOne[char] += 1
                else:
                    hashOne[char] = 1
                
                if t[idx] in hashTwo:
                    hashTwo[t[idx]] += 1
                else:
                    hashTwo[t[idx]] = 1 

        for k,v in hashOne.items():
            if (k in hashOne) & (k in hashTwo):
                if hashOne[k] != hashTwo[k]:
                    return False
            else:
                return False   
            
        return True
        