class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        n = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100
            , 'D':500, 'M':1000}
        
        for i in range(len(s)):
            if i < len(s)-1 and n[s[i]] < n[s[i+1]]:
                if s[i] == 'I' or s[i]=='X' or s[i]=='C':
                    answer += n[s[i]]*(-1)
            else:
                answer += n[s[i]]
                
        return answer

        
