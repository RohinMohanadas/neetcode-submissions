class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = defaultdict(int)
        left = 0
        right = left+1
        maxlen = 0
        length = 1
        if s == "":
            return 0
        if len(s)==1:
            return 1
        uniques[s[left]] = left
        
        while right<len(s):
            if s[right] in uniques:
                print("s[right]", s[right])
                print("right", right)
                print("----------")
                if uniques[s[right]]>=left:
                    left = uniques[s[right]]+1
                uniques[s[right]] = right
                length = right-left+1
                right+=1
                print("left",left,"right",right)
                print("length", length)
            else:
                uniques[s[right]] = right
                right +=1
                length +=1
                
            print(uniques)
            maxlen = max(maxlen,length)
            
        return maxlen