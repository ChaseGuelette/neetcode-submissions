# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive solution:
        # if root is None:
        #     return 0
        
        # left, right = 0,0
        # if root.left is None and root.right is None:
        #     return 1
        # if root.left:
        #     left = 1 + self.maxDepth(root.left)
        # if root.right:
        #     right =  1 + self.maxDepth(root.right)
        # return max(right, left)
        if root is None:
            return 0
        q = deque()
        q.append((root, 1))
        node, level = None, 0
        while q:
            node, level = q.popleft()
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
        return level



        