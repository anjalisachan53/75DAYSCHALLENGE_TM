class Solution:
    def jump(self, nums: List[int]) -> int:
        # 
        max_pos = 0
        end = 0
        steps = 0
        for i in range(len(nums) - 1):
            # 
            max_pos = max(max_pos, i + nums[i])
            # 
            #  1
            if i == end:
                end = max_pos
                steps += 1
        
        return steps
        
