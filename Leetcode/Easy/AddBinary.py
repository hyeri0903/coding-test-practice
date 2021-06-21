class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        numa = 0
        numb = 0
        answer = ''
        
        idx = 1
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1':
                numa += idx * 1
            else:
                numa += idx * 0
            idx = idx * 2
        idx = 1
        for i in range(len(b)-1, -1, -1):
            if b[i] == '1':
                numb += idx * 1
            else:
                numb += idx * 0
            idx = idx * 2
        
        total = numa+numb
        tmp = []
        if total == 0:
            return "0"
        while total > 0:
            res = total % 2
            total = total // 2
            tmp.append(res)
        
        for i in range(len(tmp)-1, -1, -1):
            answer += str(tmp[i])
            
        #return format(int(a, 2) + int(b, 2),'b')
        return answer
