#참고 : https://velog.io/@kgh732/Python-으로-푸는-Leetcode26.-Remove-Duplicates-from-Sorted-Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
                
        
        
                
        
