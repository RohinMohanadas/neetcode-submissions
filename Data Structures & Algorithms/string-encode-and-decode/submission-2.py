class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "€€€€€"
        result = ""
        print("Hello")
        for string in strs:
            result = result+string+"€"
        if result != "":
            result = result[0:-1]
        return result
    def decode(self, s: str) -> List[str]:
        if s == "€€€€€":
            print("if not s")
            return []
        strs = s.split("€")
        return strs
