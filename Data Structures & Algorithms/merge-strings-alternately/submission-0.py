class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1, len2 = len(word1), len(word2)
        res = []
        for i in range(min(len1,len2)):
            res.append(word1[i])
            res.append(word2[i])
            i+=1
        while i<len1:
            res.append(word1[i])
            i+=1
        while i<len2:
            res.append(word2[i])
            i+=1
        
        return "".join(res)
        