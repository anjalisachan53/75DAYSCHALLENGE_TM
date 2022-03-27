#Problem no.283
#Problem of Day 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length=len(nums)
        z=0
        n=0
        while n<length: 
            if (nums[n]==0):
                n=n+1
            elif (nums[n] !=0):
                if(z==n):
                    z=z+1
                    n=n+1
                else:
                    nums[z] = nums[n]
                    nums[n]=0
                    z=z+1
                    n=n+1
                
