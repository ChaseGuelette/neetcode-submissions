class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        # def backtrack(res, pos):
        #     for perm in res:
        #         #base case, return 
        #         if len(perm) >= len(nums):
        #             return 
                
        #         for i in range(perm) + 1:
        #             perm_c = perm.copy()
        #             perm_c.insert(i, nums[pos])

        def bfs(q, pos):
            if len(q[0]) == len(nums):
                print("q in return: ", q)
                return q
            
            level = len(q)
            temp = []
            for i in range(level):
                perm = q.pop()
                for j in range(len(perm) + 1):
                    perm_c = perm.copy()
                    perm_c.insert(j, nums[pos])
                    # print("current permutation: ", perm_c)
                    temp.append(perm_c)
                # print("temp: ", temp)
            q = temp
            # print(q)
            q = bfs(q, pos + 1)
            return q

                    
        res = bfs([[]], 0)
        return res