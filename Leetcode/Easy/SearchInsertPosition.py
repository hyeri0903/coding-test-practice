class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = 0
        
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = r - 1
            elif target >= nums[mid]:
                l = l + 1
        
        if nums[mid] < target:
            mid += 1
        return mid
