class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # process the strings
        results = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            results[sorted_string].append(string)
        return list(results.values())
