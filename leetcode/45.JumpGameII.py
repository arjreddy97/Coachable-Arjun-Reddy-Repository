class Solution:
    def jump(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return 0
        
        jump_count = 0
        max_reach = nums[0]
        steps = nums[0]

        for i in range(1,len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            steps -=1
            if steps == 0:
                jump_count += 1
                steps = max_reach - i
        return jump_count + 1
        


        
