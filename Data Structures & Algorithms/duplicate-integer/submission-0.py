class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = set()

        for index, value in enumerate(nums):
            if value in lookup:
                return True
            lookup.add(value)

        return False