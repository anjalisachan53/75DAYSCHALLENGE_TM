#Problem no.66
#Problem of Day1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums=0
        for i in digits:
            nums=nums*10 + i
            
            
        nums=nums+1
        l=[]
        
        while nums>0:
            l.append(nums%10)
            
            nums=nums//10
            
        return l[::-1]
