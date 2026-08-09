class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        def backtrack(total, curr, pos):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or pos >= len(nums):
                return 

            
            curr.append(nums[pos])
            backtrack(total+nums[pos], curr, pos)
            curr.pop()
            backtrack(total, curr, pos+1)


        
        backtrack(0, [], 0)
        return res