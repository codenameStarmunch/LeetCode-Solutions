class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}
        open = {"(", "[", "{"}
        new_lst = []

        for x in s:
            if x in open:
                new_lst.append(x)
            elif new_lst and x == brackets[new_lst[-1]]:
                new_lst.pop()
            else:
                return False

        return new_lst == []