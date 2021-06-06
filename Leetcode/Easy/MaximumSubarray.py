class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_sum = sum(nums)
        tmp = 0
        
        for num in nums:
            tmp = max(num, num + tmp)
            max_sum = max(tmp, max_sum)
        return max_sum
        
        
        
