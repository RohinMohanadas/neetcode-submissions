class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = [[0]*26 for i in range(len(strs))]
        added = [0]*len(strs)
        for i,s in enumerate(strs):
            for ch in s:
                chars[i][ord(ch)-ord("a")]+= 1
        
        #print(chars)
        hashMap = defaultdict(list)
        
        for idx, i in enumerate(chars):
            hashMap[str(i)].append(strs[idx])
        
        #print(hashMap)
        listet = []
        for _,v in hashMap.items():
            listet.append(v)

        return listet
 