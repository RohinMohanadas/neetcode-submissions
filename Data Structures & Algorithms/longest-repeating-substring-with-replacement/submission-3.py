class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxlen = 0

        L = 0
        for R in range(len(s)):
            counts[s[R]] += 1

            while (R-L+1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L+=1

            maxlen = max(maxlen,R-L+1)


        return maxlen
