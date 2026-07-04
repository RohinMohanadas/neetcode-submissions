class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = 201
        for string in strs:
            smallest = min(smallest,len(string))
        
        lcp = 0
        op = ""
        for i in range(smallest):
            myset = set()
            for string in strs:
                myset.add(string[i])
            if len(myset) == 1:
                op+=string[i]
                myset.clear()
            else:
                return op

        return op




        