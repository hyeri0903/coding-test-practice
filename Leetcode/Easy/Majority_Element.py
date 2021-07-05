class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)%2 != 0:
            pivot = len(nums) // 2 + 1
        else:
            pivot = len(nums) // 2
        
        dic = {}
        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
                
        for k,v in dic.items():
            if v >= pivot:
                return k
        
