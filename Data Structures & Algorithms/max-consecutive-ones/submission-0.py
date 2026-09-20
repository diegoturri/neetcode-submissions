class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for value in nums:
            if value == 1:
                count += 1
                res = max(count, res)
            if value == 0:
                count = 0

        return res