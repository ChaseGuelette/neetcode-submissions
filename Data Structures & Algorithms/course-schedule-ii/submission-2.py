class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visited, cycle = set(), set()
        order = []
        preReq = {i: [] for i in range(numCourses)}

        for crs, item in prerequisites:
            preReq[crs].append(item)

        #a course has 3 possible states 
        # visited - added to output
        # visiting - crs not added to output, but added to cycle 
        # unvisited - not added to output or cycle 
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            
            for req in preReq[node]:
                val = dfs(req)
                if not val:
                    return False
                
            cycle.remove(node)
            visited.add(node)
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i): 
                return []
        return order 


        #I think that an important thing to note in these problems
        #That i dont really get 
        #is that numCourses, which is an int, is in a way a list 
        #if numCourses = 8, then there are 8 nodes in the prerequisites list
        #and we need to check all of them, and they can be disconnected 

        #create visited set, order return list, and preReq hashmap 
            #set preReq list to none, since that implies we can do it 
            #add to order since done with list 
            #remove from visited set so other recursions can work
        #call dfs on every node, we could have disconnected nodes
        #if dfs returns false, theres a cycle and we cant get all classes
        #return empty list. 
        #if dfs finished for every node, order should have required order 
        #return 

        