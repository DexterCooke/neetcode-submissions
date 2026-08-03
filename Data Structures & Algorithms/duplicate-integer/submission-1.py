class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pool = set()
        for index, value in enumerate(nums):
            if value in pool:
                return True
            pool.add(value)
        return False

