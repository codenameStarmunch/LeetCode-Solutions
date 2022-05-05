
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for x in range(len(strs[0])):
            for string in strs[1:]:
                if x >= len(string) or string[x] != strs[0][x]:
                    return strs[0][:x]

        return strs[0]

    