class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                # shorten the prefix from right side
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix            
