
class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {"(": ")", "[": "]", "{": "}"}
        open_brackets = {"(", "[", "{"}
        result = []

        for x in s:
            if x in open_brackets:
                result.append(x)
            elif result and x == closed_brackets[result[-1]]:
                result.pop()
            else:
                return False

        return  == []
