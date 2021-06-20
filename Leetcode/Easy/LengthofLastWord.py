class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        tmp = s.split(" ")
        
        i = len(tmp)-1
        if tmp[i] == "":
            while tmp[i]=="":
                i -=1
                if i == 0:
                    break
        
        
        return len(tmp[i])
