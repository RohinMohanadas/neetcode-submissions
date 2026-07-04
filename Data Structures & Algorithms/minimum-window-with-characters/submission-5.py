class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counts = defaultdict(int)
        substr = defaultdict(int)

        for i in t:
            counts[i]+=1

        have, need = 0, len(counts)

        l,r = 0,0

        minlength = float("inf")
        minleft = 0
        minright = len(s)-1

        for r in range(len(s)):
        #for l in range(0,len(s)-need):
            print("l--r", l,r)
            substr[s[r]]+=1
            if s[r] in counts and substr[s[r]] == counts[s[r]]:
                have+=1      

            while have == need:
                print("have what i need")
                if minlength > r-l+1:
                    minlength = r-l+1
                    minleft = l
                    minright = r
                    print(l,r,minlength)
                substr[s[l]]-=1
                if s[l] in substr and substr[s[l]] < counts[s[l]]:
                    have-=1            
                l+=1       
                             
            print(substr)    

            
        return s[minleft:minright+1] if minlength!=float("inf") else ""
