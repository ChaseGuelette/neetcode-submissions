class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # def bfs(q, pos):
        #     if len(q[0]) == len(nums):
        #         return q
            
        #     level = len(q)
        #     temp = []
        #     for i in range(level):
        #         perm = q.pop()
        #         for j in range(len(perm) + 1):
        #             perm_c = perm.copy()
        #             perm_c.insert(j, nums[pos])
        #             temp.append(perm_c)
        #     q = temp
        #     q = bfs(q, pos + 1)
        #     return q

                    
        # res = bfs([[]], 0)
        # return res

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res 