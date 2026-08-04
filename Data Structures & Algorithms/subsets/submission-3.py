class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        def backtrack(nums, retList, index):

            if index >= len(nums):
                return res.append(retList.copy())
            #append
            retList.append(nums[index])
            backtrack(nums, retList, index + 1)
            retList.pop()
            #dont add
            backtrack(nums, retList, index + 1)

        backtrack(nums, [], 0)
        return res
        