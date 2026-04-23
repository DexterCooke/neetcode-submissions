class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for c in range(len(nums)):

            val = target - nums[c]

            if val in map:
                return [map[val], c]

            else:
                map[nums[c]] = c