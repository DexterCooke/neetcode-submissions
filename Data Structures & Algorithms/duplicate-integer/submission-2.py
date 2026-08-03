class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for index, value in enumerate(nums):
            if value in seen:
                return True
            seen.add(value)

        return False