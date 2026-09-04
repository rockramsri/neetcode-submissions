# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def goDeep(head,level,m):
            if head is None:
                return None
            if len(m)<level+1:
                m.append([])
            m[level].append(head.val)

            goDeep(head.left,level+1,m)
            goDeep(head.right,level+1,m)
        
        m=[]
        goDeep(root,0,m)
        #print(m)
        return m

