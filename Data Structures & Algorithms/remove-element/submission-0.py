class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        empty = 0

        for num in nums:
            if num != val:
                nums[empty] = num
                empty += 1
        
        res = empty
        return res
        

                
