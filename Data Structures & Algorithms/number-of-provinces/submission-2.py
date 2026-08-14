class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adjList = [[] for i in range(len(isConnected))]
        rows, cols = len(isConnected), len(isConnected[0])

        for i in range(rows):
            for j in range(cols):
                #i is the node number
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
        
        #okay so now we have the adj list 
        N = len(adjList)
        par = [i for i in range(N)]
        rank = [1] * N 

        #This means that n isnt its own parent
        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n] 


        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False 
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True 
        
        provinces = N
        for i, node in enumerate(adjList):
            for connection in node:
                if union(i, connection):
                    provinces -= 1

        return provinces

        
        