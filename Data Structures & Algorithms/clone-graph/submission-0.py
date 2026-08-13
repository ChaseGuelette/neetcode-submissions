"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #hashmap to track the nodes we have created
        oldToNew = {}


        def dfs(node):
            #if the node has already been cloned, we return the already copied 
            #version of that node
            if node in oldToNew:
                return oldToNew[node]
            
            #normal work. We copy the node, and initlize it with the og's value
            copy = Node(node.val)
            #append the copy to the hashmap of cloned nodes
            oldToNew[node] = copy
            #take each neighbor, and add it to the list of neighbors for the 
            #the current node
            for neigh in node.neighbors:
                #this dfs will recurse to the next node, and eventually return a 
                #copy node to be appended to the neighbor
                copy.neighbors.append(dfs(neigh))
            
            #once we've made the copy and created the list of its neighbors, 
            #return the copy
            return copy
        
        return dfs(node) if node else None

