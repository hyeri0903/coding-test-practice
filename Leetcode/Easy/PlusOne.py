class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        idx = 1
        
        for i in range(len(digits)-1, -1, -1):
            num += digits[i] * idx
            idx = idx * 10
            
        num += 1
        
        res = []
        while num > 0:
            res.append(num%10)
            num = num//10

        answer = []
        for i in range(len(res)-1, -1, -1):
            answer.append(res[i])
       
        return answer
        
