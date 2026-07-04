class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i in ["{","[","("]:
                res.append(i)
            elif i == "}":
                if not res or res.pop() != "{":
                    return False
            elif i == ")":
                if not res or res.pop() != "(":
                    return False
            else:
                if not res or res.pop() != "[":
                    return False

        return not res   
        