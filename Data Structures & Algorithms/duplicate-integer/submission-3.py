class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for index, val in enumerate(nums):
            if val in seen:
                return True
            seen.add(val)

        return False