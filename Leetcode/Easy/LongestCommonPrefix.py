class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        n = len(strs)
        
        if n == 0:
            return ""
        if n== 1:
            return strs[0]
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        end = min(len(first), len(last))
        
        while(i < end and first[i] == last[i]):
            pre += first[i]
            i+=1
            
        return pre
