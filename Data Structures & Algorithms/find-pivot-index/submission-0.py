class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        fullSum = sum(nums)
        leftSum = 0
        print(fullSum)
        for i in range(len(nums)):
            if (fullSum - nums[i]) == leftSum:
                return i 
            leftSum += nums[i]
            fullSum -= nums[i]
            print(leftSum, fullSum)
        return -1
        