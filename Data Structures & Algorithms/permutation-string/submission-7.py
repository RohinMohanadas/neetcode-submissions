class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        l = 0
        r = s1len-1
        set2hash = defaultdict(int)
        set1hash = defaultdict(int)

        for i in s1:
            set1hash[i]+=1
        
        for i in s2[l:r+1]:
            set2hash[i]+=1

        print(set1hash)



        
        while r < len(s2):
            notfound = False  
            for k,v in set2hash.items():
                print(set2hash)
                if set2hash[k] == set1hash[k]:
                    continue
                else:
                    notfound = True
                    print("Here")
                    break

            if notfound == False:
                return True
            

            set2hash[s2[l]]-=1
            l+=1
            r+=1
            if r <len(s2):
                set2hash[s2[r]]+=1
            
            
        return False
        