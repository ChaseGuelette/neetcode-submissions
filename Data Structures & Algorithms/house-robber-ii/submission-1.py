class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(nums: List[int]):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        n = len(nums)
        one = nums[0:(n-1)]
        two = nums[1:n]
        print(one, two)
        return max(dfs(one), dfs(two))

        