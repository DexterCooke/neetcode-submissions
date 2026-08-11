class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = defaultdict(list)

        for index, val in enumerate(strs):
            sorted_word = ''.join(sorted(val))
            lookup[sorted_word].append(val)

        return list(lookup.values())
        