# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        head=root

        p,q=min(p.val,q.val),max(p.val,q.val)
        while head!=None:
            if (head.val==p or head.val==q) or (head.val >= p and head.val <= q):
                return head
            if head.val > p and head.val > q:
                head=head.left
            else:
                head=head.right
        
