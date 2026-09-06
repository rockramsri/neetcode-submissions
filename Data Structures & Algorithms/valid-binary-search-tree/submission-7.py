# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid=True
        def depth(tempNode,maxfollowVal,minfollowVal):
            if tempNode==None or self.valid==False:
                return 
            #print(self.valid,tempNode.val)
            if tempNode.left!=None:
                if tempNode.left.val<tempNode.val and tempNode.left.val>maxfollowVal:
                    depth(tempNode.left,maxfollowVal,min(minfollowVal,tempNode.val))
                else:
                    self.valid=False
            #print(self.valid,tempNode.left.val<tempNode.val)
            if tempNode.right!=None:
                if tempNode.right.val>tempNode.val and tempNode.right.val<minfollowVal:
                    depth(tempNode.right,max(maxfollowVal,tempNode.val),minfollowVal)
                else:
                    self.valid=False
        depth(root,-float('inf'),float('inf'))
        return self.valid
