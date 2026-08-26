class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        store = {}
        minSteps = 10000000000

        def dfs(num):
            print("step")

            if num in store:
                return store[num]
            if num == amount:
                store[num] = 0
                return 0
            if num > amount:
                store[num] = -1
                return -1
            
            store[num] = -1 
            for coin in coins:
                stepsToEnd = dfs(num + coin)
                if stepsToEnd == -1:
                    continue 

                candidate = 1 + stepsToEnd

                if candidate < store[num] or store[num] == -1:
                    store[num] = candidate
            return store[num]
            

        
        # for coin in coins:
        #     minSteps = dfs(coin)
            
        # if minSteps == 10000000000:
        #     return -1
        # return minSteps
        return dfs(0)
        