# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        head=root
        cMax=-101
        self.gNodeCount=0
        def depth(tempNode,currentMax):
            
            if tempNode==None:
                return
            #print(self.gNodeCount,currentMax,tempNode.val)
            #print(self.gNodeCount,currentMax,tempNode.val)
            if currentMax<=tempNode.val:
                self.gNodeCount+=1    
                currentMax=tempNode.val
            depth(tempNode.left,currentMax)
            depth(tempNode.right,currentMax)
            
        depth(head,cMax)
        #print(self.gNodeCount)
        return self.gNodeCount





        
            

