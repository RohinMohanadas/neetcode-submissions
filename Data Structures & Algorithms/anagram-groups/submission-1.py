class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        if len(string1)!=len(string2):
            return False
        else:
            hashMap1 = defaultdict(int)
            for i in string1:
                hashMap1[i] += 1
            
            hashMap2 = defaultdict(int)
            for i in string2:
                hashMap2[i] += 1

            for i in string1:
                if hashMap1[i] != hashMap2[i]:
                    return False
            
            return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {v:True for v in strs}
        print(hashMap)
        outputList = []
        for i,string in enumerate(strs):
            anaList = []
            if hashMap[string]:
                anaList.append(string)
                for string2 in strs[i+1:]:
                    if self.isAnagram(string, string2):
                        anaList.append(string2)
                        hashMap[string2]=False
                hashMap[string]=False
            print(anaList)
            if anaList:
                outputList.append(anaList)
        return outputList
                


