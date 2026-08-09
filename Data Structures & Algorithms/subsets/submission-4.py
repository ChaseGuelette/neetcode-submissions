class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        def backtrack(curr, pos):
            if pos >= len(nums):
                res.append(curr.copy())
                return 
            
            #do work, backtrack
            curr.append(nums[pos])
            backtrack(curr, pos+1)
            #undo work, backtrack 
            curr.pop()
            backtrack(curr, pos+1)
            #exit
            return 
        
        backtrack([], 0)
        return res