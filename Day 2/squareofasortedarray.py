#977. Squares of a Sorted Array
#Day 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        i=0
        j=len(nums)-1
        
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                s.append(nums[i]*nums[i])
                i+=1
            else:
                s.append(nums[j]*nums[j])
                j-=1
        return s[::-1]
        
